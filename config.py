# Config
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

# App
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', '8080'))
API_NAME = 'Meet Room Watch project RESTful API'
API_VERSION = '0.4.0'

#Google API
GC_CLIENT_SECRET = os.path.join(basedir, 'client_secret.json')
GC_CLIENT_CREDENTIALS = os.path.join(basedir, 'calendar-credentials.json')
GC_SYNC_INTERVAL = datetime.timedelta(minutes = 1) # Limit minimal re-sync time interval in minutes
GC_LAST_SYNC = datetime.datetime.utcnow()

# check dev.environment
if bool(os.getenv('FLASK_DEBUG')):
    DEBUG = True
else:
    DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DB/meet-room.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
if DEBUG:
    SQL_DEBUG = True
else:
    SQL_DEBUG = False

#CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'