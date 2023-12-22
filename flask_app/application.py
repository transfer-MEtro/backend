import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .views import main_views


print("Initializing application...")
load_dotenv()

SERVER_PORT = os.environ.get('SERVER_PORT')

application = Flask(__name__)
application.register_blueprint(main_views.bp)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == "__main__":
    application.run(port=SERVER_PORT)
