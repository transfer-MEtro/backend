from flask import Blueprint, jsonify
import pymysql
import realtime_arrival_list

bp = Blueprint('main', __name__, url_prefix='/')


def insert_data(station):
    # Insert data into the table
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root123!', db='metro_db', charset='utf8')
    cursor = db.cursor()

    # Get the realtime arrival list
    arrival_list = realtime_arrival_list.extract_json(station)

    insert_sql_template = '''INSERT INTO metro_db.Subway
                (btrainNo, subwayId, statnFid, statnTid, statnId, statnNm, barvlDt)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                subwayId = VALUES(subwayId),
                statnFid = VALUES(statnFid),
                statnTid = VALUES(statnTid),
                statnId = VALUES(statnId),
                statnNm = VALUES(statnNm),
                barvlDt = VALUES(barvlDt);'''

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
                btrainNo VARCHAR(100) PRIMARY KEY,
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
def insert():
    insert = insert_data("신촌")
    return insert


@bp.route('/insert/<line>')
def insert_line(line):
    line_2 = ['시청', '을지로입구', '을지로3가', '을지로4가', '동대문역사문화공원', '신당', '상왕십리', '왕십리', '한양대', '뚝섬', '성수', '건대입구', '구의', '강변', '잠실나루', '잠실', '잠실새내', '종합운동장', '삼성', '선릉', '역삼', '강남', '교대', '서초', '방배',
              '사당', '낙성대', '서울대입구', '봉천', '신림', '신대방', '구로디지털단지', '대림', '신도림', '문래', '영등포구청', '당산', '합정', '홍대입구', '신촌', '이대', '아현', '충정로', '용답', '신답', '용두', '신설동', '도림천', '양천구청', '신정네거리', '까치산']

    for station in line_2:
        insert_data(station)
    return "line " + line


@bp.route('/json_test')
def hello_json():
    data = {'name': 'Aaron', 'family': 'Byun'}
    return jsonify(data)


@bp.route('/server_info')
def server_json():
    data = {'server_name': '0.0.0.0', 'server_port': '8080'}
    return jsonify(data)
