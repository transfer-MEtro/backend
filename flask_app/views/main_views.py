from flask import Blueprint, jsonify
import pymysql

bp = Blueprint('main', __name__, url_prefix='/')


def init_db():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root123!', db='metro_db', charset='utf8')
    cursor = db.cursor()
    db_sql = '''CREATE DATABASE IF NOT EXISTS metro_db default CHARACTER SET UTF8;'''
    table_sql = '''CREATE TABLE IF NOT EXISTS metro_db.Subway
            (
                btrainNo INT PRIMARY KEY,
                subwayId INT NOT NULL,
                statnFid INT NOT NULL,
                statnTid INT NOT NULL,
                statnId INT NOT NULL,
                statnNm VARCHAR(32) NOT NULL,
                barvlDt INT NOT NULL
            ) ENGINE = INNODB;'''
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


@bp.route('/bye')
def bye_flask():
    return 'Bye, Flask!'


@bp.route('/json_test')
def hello_json():
    data = {'name': 'Aaron', 'family': 'Byun'}
    return jsonify(data)


@bp.route('/server_info')
def server_json():
    data = {'server_name': '0.0.0.0', 'server_port': '8080'}
    return jsonify(data)
