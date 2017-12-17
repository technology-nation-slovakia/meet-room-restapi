# Config
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

# App
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', '8080'))
API_NAME = 'Meet Room Watch project RESTful API'
API_VERSION = '0.4.2'

# check dev.environment
if bool(os.getenv('FLASK_DEBUG')):
    DEBUG = True
else:
    DEBUG = False

#Google API
GC_CLIENT_SECRET = os.path.join(basedir, 'client_secret.json')
GC_CLIENT_CREDENTIALS = os.path.join(basedir, 'calendar-credentials.json')

if DEBUG:
    GC_SYNC_INTERVAL = datetime.timedelta(seconds = 20) # Limit minimal re-sync time interval for GC
else:
    GC_SYNC_INTERVAL = datetime.timedelta(minutes = 1)
GC_LAST_SYNC = datetime.datetime.utcnow() - GC_SYNC_INTERVAL

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DB/meet-room.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQL_DEFAULT_FIELDS='''id, name, description, strftime('%Y-%m-%dT%H:%M:%SZ', start_date) as start_date,
strftime('%Y-%m-%dT%H:%M:%SZ', end_date) as end_date, place_id'''
if DEBUG:
    SQL_DEBUG = True
else:
    SQL_DEBUG = False

