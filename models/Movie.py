from app import db


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    poster_url = db.Column(db.String(256))
    price = db.Column(db.Float(2))
    duration = db.Column(db.Integer)
    session_start = db.Column(db.TIMESTAMP)
    session_date = db.Column(db.TIMESTAMP)
