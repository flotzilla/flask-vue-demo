from db import db


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "%d - %s" % (self.id, self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }