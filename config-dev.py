# Development Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))


HOST = '0.0.0.0'
PORT = 8080
API_NAME = 'Meet Room Watch project RESTful API'
API_VERSION = '0.1.0'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DB/meet-room.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False