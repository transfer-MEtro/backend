from flask import Blueprint, jsonify
import pymysql

bp = Blueprint('main', __name__, url_prefix='/')


def db_connector():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root123!', db='pbj_db', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT * FROM pbj_db.Score;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)


@bp.route('/')
def index():
    a = db_connector()
    return a


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
