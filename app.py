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

class Logs(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    details = db.Column(db.String(5000))

class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    msg = db.Column(db.String(5000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    data = Logs.query.all()
    return render_template('logs.html',data=data)

@app.route('/addlogs',methods=['GET','POST'])
def addlogs():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        date = request.form['date']
        time = request.form['time']
        details = request.form['details']
        data = Logs(name=name,color=color,date=date,time=time,details=details)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('addlogs'))
    return render_template('addlogs.html')

@app.route('/',methods=['POST'])
def contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    msg = request.form['msg']
    contact = Contact(name=name,email=email,phone=phone,msg=msg)
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/contact',methods=['GET'])
def getcontact():
    data = Contact.query.all()
    return render_template('contact.html',data=data)

if __name__ == '__main__':
    db.create_all()
    TEMPLATES_AUTO_RELOAD = True
    app.run(threaded=True, port=8000,debug=True)
