from flask import current_app as app,request, jsonify,render_template, redirect, url_for,session,message_flashed,send_file,send_from_directory
from flask import render_template,jsonify
from ..models import db
import simplejson
import json
import simplejson
import json
import random
import string
import uuid
import os
import urllib.request
from datetime import datetime
from ..models import Logs,Todos,Contact
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template

# Blueprint Configuration
portfolio = Blueprint('portfolio',__name__,
                    template_folder='templates',
                    url_prefix='/'
                    )

@portfolio.route('/')
def index():
    return render_template('/portfolio/main/index.html')

@portfolio.route('/logs')
def logs():
    data = Logs.query.all()
    datatodos = Todos.query.all()
    return render_template('portfolio/main/logs.html',data=data,datatodos=datatodos)

@portfolio.route('/addlogs',methods=['GET','POST'])
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
        return redirect(url_for('portfolio.addlogs'))
    return render_template('portfolio/main/addlogs.html')

@portfolio.route('/addtodos',methods=['GET','POST'])
def addtodos():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        date = request.form['date']
        time = request.form['time']
        details = request.form['details']
        data = Todos(name=name,color=color,date=date,time=time,details=details)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('portfolio.addlogs'))
    return render_template('portfolio/main/addlogs.html')

@portfolio.route('/',methods=['POST'])
def contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    msg = request.form['msg']
    contact = Contact(name=name,email=email,phone=phone,msg=msg)
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('index'))

@portfolio.route('/admin',methods=['GET'])
def getcontact():
    data = Contact.query.all()
    return render_template('admin/admin.html',data=data)
