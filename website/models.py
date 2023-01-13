from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Player(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150), unique=False)
    lastname = db.Column(db.String(150), unique=False)
    pin = db.Column(db.String(150), unique=False)