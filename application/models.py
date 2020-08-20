from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Logs(db.Model):
    __tablename__ = 'logs'
    log_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    details = db.Column(db.String(5000))

class Todos(db.Model):
    __tablename__ = 'todos'
    todos_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    details = db.Column(db.String(5000))

class Contact(db.Model):
    __tablename__ = 'contacts'
    contact_id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    msg = db.Column(db.String(5000))