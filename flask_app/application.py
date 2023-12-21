from flask import Flask
from flask_app.views import main_views


def create_app():
    app = Flask(__name__)

    # 블루프린트
    app.register_blueprint(main_views.bp)

    return app
