from flask import Flask, request, jsonify,render_template, redirect, url_for,session,message_flashed,send_file,send_from_directory
# from models import Exams
import simplejson
import json
import random
import string
import uuid
import os
import urllib.request
from config import Config
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = 'worldsucks'
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'))
Session = sessionmaker(bind=engine)
ses = Session()


class Feedback(db.Model):
    feedback_id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50))
    msg = db.Column(db.String(5000))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/logs')
def logs():
    return render_template('logs.html')
          
if __name__ == '__main__':
    db.create_all()
    TEMPLATES_AUTO_RELOAD = True
    app.run(threaded=True, port=8000,debug=True)
