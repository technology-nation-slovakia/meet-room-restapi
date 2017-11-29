import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime

from app import app

def get_credentials():
    store = Storage(app.config['GC_CLIENT_CREDENTIALS'])
    credentials = store.get()
    if not credentials or credentials.invalid:
        print('Missed or Invalid Google Calendar API credentials')
        return None
    return credentials

def today_events(calendar_id):
    credentials = get_credentials()
    if not credentials:
        return None

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    #now = datetime.datetime.utcnow().isoformat()  + 'Z' # 'Z' indicates UTC time
    timeMin = datetime.datetime.utcnow().strftime("%Y-%m-%dT00:00:00Z")
    timeMax = datetime.datetime.utcnow().strftime("%Y-%m-%dT23:59:59Z")

    eventsResult = service.events().list(
        calendarId=calendar_id, timeMin=timeMin, timeMax=timeMax, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    return events

