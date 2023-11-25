from flask import Blueprint, jsonify
import pymysql
import realtime_arrival_list

bp = Blueprint('main', __name__, url_prefix='/')


def insert_data():
    # Insert data into the table
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root123!', db='metro_db', charset='utf8')
    cursor = db.cursor()

    # Get the realtime arrival list
    arrival_list = realtime_arrival_list.extract_json()

    insert_sql_template = '''INSERT INTO metro_db.Subway
                (btrainNo, subwayId, statnFid, statnTid, statnId, statnNm, barvlDt)
                VALUES (%s, %s, %s, %s, %s, %s, %s);'''

    for item in arrival_list:
        # Extract variables from each dictionary in the list
        btrainNo = item['btrainNo']
        subwayId = item['subwayId']
        statnFid = item['statnFid']
        statnTid = item['statnTid']
        statnId = item['statnId']
        statnNm = item['statnNm']
        barvlDt = item['barvlDt']

        # Print the SQL statement
        cursor.execute(insert_sql_template, (btrainNo, subwayId,
                       statnFid, statnTid, statnId, statnNm, barvlDt))
        # Commit the transaction
        db.commit()
    db.close()
    return f"Number of rows inserted: {cursor.rowcount}"


def init_db():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root123!', db='metro_db', charset='utf8mb4')
    cursor = db.cursor()
    db_sql = '''CREATE DATABASE IF NOT EXISTS metro_db default CHARACTER SET UTF8;'''
    table_sql = '''CREATE TABLE IF NOT EXISTS metro_db.Subway
            (
                btrainNo INT PRIMARY KEY,
                subwayId INT NOT NULL,
                statnFid INT NOT NULL,
                statnTid INT NOT NULL,
                statnId INT NOT NULL,
                statnNm VARCHAR(100) CHARACTER SET utf8mb4,
                barvlDt INT NOT NULL
            ) ENGINE = INNODB DEFAULT CHARSET=utf8mb4;'''
    cursor.execute(db_sql)
    cursor.execute(table_sql)
    result = cursor.fetchall()
    db.close()
    return str(result)


@bp.route('/')
def index():
    db_init = init_db()
    return db_init


@bp.route('/hello')
def hello_flask():
    return 'Hello, Flask!'


@bp.route('/insert')
def bye_flask():
    insert = insert_data()
    return insert


@bp.route('/json_test')
def hello_json():
    data = {'name': 'Aaron', 'family': 'Byun'}
    return jsonify(data)


@bp.route('/server_info')
def server_json():
    data = {'server_name': '0.0.0.0', 'server_port': '8080'}
    return jsonify(data)
