from random import randint

from flask import Blueprint, jsonify

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api')


@api_v1.route('/')
def index():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)
