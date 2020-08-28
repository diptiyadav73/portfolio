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

@blogs.route('/author/<id>', methods=['POST','GET'])
def authors(id):
    author = Author.query.filter_by(slug=id).first()
    return render_template('/blogs/main/authordetails.html', data=author)
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
@blogs.route('/receiver', methods=['POST'])
def receiver():
    blog = (request.json)
    # print (blog['title'])
    pre = PreBlogs(title=request.form['title'],author=request.form['author'],series=request.form['series'],time=request.form['time'],date=request.form['date'],tag=request.form['tags'],meta=request.form['meta'],content=request.form['editor'],slug=request.form['slug'])
    db.session.add(pre)
    db.session.commit()
    return redirect(url_for('blogs.preblogs'))

@blogs.route('/preblogs', methods=['POST','GET'])
def preblogs():
    blog = PreBlogs.query.all()
    return render_template('/blogs/main/preblogs.html',blogs=blog)

@blogs.route('/preblogview/<id>', methods=['POST','GET'])
def preblogview(id):
    blog = PreBlogs.query.filter_by(id=id).first()
    return render_template('/blogs/main/preblogview.html',blogs=blog)