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
# from ..models import 
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
