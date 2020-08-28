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

class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    headerimg = db.Column(db.String(100))
    title = db.Column(db.String(100))
    series = db.Column(db.String(100))
    author = db.Column(db.String(100))
    time = db.Column(db.String(100))
    date = db.Column(db.String(100))
    tag = db.Column(db.String(100))
    meta = db.Column(db.String(100))
    content = db.Column(db.String(100000))
    img = db.Column(db.String(300))
    slug = db.Column(db.String(300),unique=True)

class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    series = db.Column(db.String(100))
    slug = db.Column(db.String(300),unique=True)

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    website = db.Column(db.String(300))
    quotes = db.Column(db.String(300))
    slug = db.Column(db.String(300),unique=True)
    
class PreBlogs(db.Model):
    __tablename__ = 'preblogs'
    id = db.Column(db.Integer, primary_key=True)
    headerimg = db.Column(db.String(100))
    title = db.Column(db.String(100))
    series = db.Column(db.String(100))
    author = db.Column(db.String(100))
    time = db.Column(db.String(100))
    date = db.Column(db.String(100))
    tag = db.Column(db.String(100))
    meta = db.Column(db.String(100))
    content = db.Column(db.String(100000))
    img = db.Column(db.String(300))
    slug = db.Column(db.String(300),unique=True)
