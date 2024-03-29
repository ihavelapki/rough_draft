print('import models', __name__)
from education.authserver import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=True)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('Note')
    user_info = db.relationship('UserInfo')


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    second_name = db.Column(db.String(150))
    user_address = db.Column(db.String(150))
    user_avatar = db.Column(db.String(150))
    user_note = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
