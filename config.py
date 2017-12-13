# Config
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

# App
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', '8080'))
API_NAME = 'Meet Room Watch project RESTful API'
API_VERSION = '0.4.0'

# check dev.environment
if bool(os.getenv('FLASK_DEBUG')):
    DEBUG = True
else:
    DEBUG = False

#Google API
GC_CLIENT_SECRET = os.path.join(basedir, 'client_secret.json')
GC_CLIENT_CREDENTIALS = os.path.join(basedir, 'calendar-credentials.json')

GC_LAST_SYNC = datetime.datetime.utcnow()
if DEBUG:
    GC_SYNC_INTERVAL = datetime.timedelta(seconds = 10) # Limit minimal re-sync time interval in minutes
else:
    GC_SYNC_INTERVAL = datetime.timedelta(minutes = 5)


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DB/meet-room.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQL_DEFAULT_FIELDS='''id, name, description, strftime('%Y-%m-%dT%H:%M:%SZ', start_date) as start_date,
strftime('%Y-%m-%dT%H:%M:%SZ', end_date) as end_date, place_id'''
if DEBUG:
    SQL_DEBUG = True
else:
    SQL_DEBUG = False

#CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'