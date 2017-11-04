from random import randint

from sqlalchemy.orm import lazyload
from sqlalchemy.orm.exc import NoResultFound

from db import db

from flask import Blueprint, jsonify

from models.Genre import Genre
from models.Movie import Movie

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api')


@api_v1.route('/')
def index():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@api_v1.route('/movies/',  methods=['GET'])
def movies_list():
    movies = [i.serialize for i in db.session.query(Movie).options(lazyload('children')).all()]
    if len(movies) == 0:
        response = {}
    else:
        response = movies

    return jsonify(
        {
            'movies': response
        }
    )


@api_v1.route('/genres',  methods=['GET'])
def get_genres():
    genres = [i.serialize for i in db.session.query(Genre).all()]
    response = {
        'genres': genres
    }
    return jsonify(response)


@api_v1.route('/movies/<id>',  methods=['GET'])
def get_movie(id):
    was_found = 'found'
    try:
        movie = db.session.query(Movie).filter_by(id=id).options(lazyload('children')).one()
        movie = movie.serialize
    except NoResultFound:
        movie = None
        was_found = 'not found'

    return jsonify({
        'status': was_found,
        'movie': movie
    })
