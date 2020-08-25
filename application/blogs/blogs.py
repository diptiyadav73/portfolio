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
from ..models import Series,Author,PreBlogs
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template

# Blueprint Configuration
blogs = Blueprint('blogs',__name__,
                    template_folder='templates',
                    url_prefix='/blogs'
                    )

@blogs.route('/')
def index():
    return render_template('/blogs/main/index.html')

@blogs.route('/staticupload')
def staticupload():
    return render_template('/blogs/main/staticupload.html')

@blogs.route('/author', methods=['POST','GET'])
def author():
    if request.method == 'POST':
        author = Author(name = request.form['name'], website = request.form['website'],quotes = request.form['quotes'],slug = request.form['slug'])
        db.session.add(author)
        db.session.commit()
    author = Author.query.all()
    return render_template('/blogs/main/author.html', data=author)

@blogs.route('/series', methods=['POST','GET'])
def series():
    if request.method == 'POST':
        series = Series(series = request.form['series'], title = request.form['title'], slug = request.form['slug'])    
        db.session.add(series)
        db.session.commit()
    series = Series.query.all()
    return render_template('/blogs/main/series.html',data = series)

@blogs.route('/addblog')
def addblogs():
    author = Author.query.all()
    series = Series.query.all()
    return render_template('/blogs/main/addblogs.html',
                            author = author,
                            series = series
                            )
@app.route('/receiver', methods=['POST'])
def receiver():
    blog = json.dumps(request.json)
    pre = PreBlogs(title=blog['title'],author=blog['author'],series=blog['series'],time=blog['time'],date=blog['date'],tag=tags['tags'],meta=blog['meta'],editor=blog['editor'],slug=blog['slug'])
    db.session.add(pre)
    db.session.commit()
    return 'OK', 200

@blogs.route('/preblogs', methods=['POST','GET'])
def preblogs():
    blog = PreBlogs.query.all()
    return render_template('/blogs/main/preblogs.html',blogs=blog)
