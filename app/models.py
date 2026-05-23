from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # admin/user


class Singer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    number = db.Column(db.Integer)


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    round_id = db.Column(db.Integer)

    type = db.Column(db.String(10))  # Solo/Duet
    singer1 = db.Column(db.Integer)
    singer2 = db.Column(db.Integer, nullable=True)

    language = db.Column(db.String(50))
    song_title = db.Column(db.String(200))
    movie = db.Column(db.String(200))
    track_link = db.Column(db.Text)

    status = db.Column(db.String(20), default="Pending")
    queue_order = db.Column(db.Integer)
