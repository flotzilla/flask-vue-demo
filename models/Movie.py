from app import db
from models import Genre

movie_genres_table = db.Table('movie_genre',
                              db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                              db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
                              )


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    poster_url = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float(2), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    session_start = db.Column(db.TIMESTAMP, nullable=False)
    session_date = db.Column(db.TIMESTAMP, nullable=False)

    children = db.relationship("Genre",
                               secondary=movie_genres_table)
