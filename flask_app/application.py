import os
from dotenv import load_dotenv
from flask import Flask

from .views import main_views


print("Initializing application...")
load_dotenv()

SERVER_PORT = os.environ.get('SERVER_PORT')

application = Flask(__name__)
application.register_blueprint(main_views.bp)


if __name__ == "__main__":
    application.run(port=SERVER_PORT)
