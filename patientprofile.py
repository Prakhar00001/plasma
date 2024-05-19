from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import secrets

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    mobile_number = db.Column(db.String(16), nullable=False)
    email_id = db.Column(db.String(128), unique=True, nullable=False)
    profile_picture = db.Column(db.BLOB, nullable=True)
    medical_records = db.Column(db.Text, nullable=True)
    symptoms = db.Column(db.Text, nullable=True)