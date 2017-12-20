# Main APP module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app)

app.config.from_object('config')
db = SQLAlchemy(app)

# Enable foreign-keys support in sqlite!
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

from app import api, admin, dbtest

