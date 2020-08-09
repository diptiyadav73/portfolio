import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SECRET_KEY = 'worldsucks'

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

