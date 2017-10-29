from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/')
def index():
    response = {
        'auth': 'should init'
    }
    return jsonify(response)
