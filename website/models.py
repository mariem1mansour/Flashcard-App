from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    full_name = db.Column(db.String(50))
    flashcards = db.relationship('Flashcard')