from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_flask():
    return 'Hello, Flask!'


@bp.route('/bye')
def bye_flask():
    return 'Bye, Flask!'


@bp.route('/')
def index():
    return 'Flask index'
