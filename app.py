from flask import Flask, jsonify, Blueprint
from flask import render_template

from flask_cors import CORS

from api.api import api_v1
from api.auth import auth

app = application = Flask("Ticker-booking",
                          static_folder="./dist/static",
                          template_folder="./dist")

CORS(api_v1)
app.register_blueprint(api_v1)
app.register_blueprint(auth)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
