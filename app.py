from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from api.api import api_v1
from api.auth import auth
import config
import logging

logger = None


def init_logger():
    global logger
    logger = logging.getLogger('Ticket booking logger')
    fh = logging.FileHandler('app.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(fh)


def init_blue_prints():
    CORS(api_v1)
    app.register_blueprint(api_v1)
    app.register_blueprint(auth)


app = Flask("Ticker-booking",
            static_folder="./dist/static",
            template_folder="./dist")
app.debug = config.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
api = Api(app)


# main route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    init_logger()
    init_blue_prints()
    app.run('localhost', 5000, app, use_debugger=True, use_reloader=True)
