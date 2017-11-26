# Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', '8080'))
API_NAME = 'Meet Room Watch project RESTful API'
API_VERSION = '0.2.0'

if bool(os.getenv('FLASK_DEBUG')):
    DEBUG = True
else:
    DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DB/meet-room.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

#CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'