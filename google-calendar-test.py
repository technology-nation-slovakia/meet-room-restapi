#!/usr/bin/env python

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import json

import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():

    credential_path = os.path.join(os.getcwd(),'calendar-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES,redirect_uri='http://localhost')
        flow.user_agent = APPLICATION_NAME
        auth_uri = flow.step1_get_authorize_url()
        print("Open foolowing url in browser: ",auth_uri)
        code = input('Input code: ')
        credentials = flow.step2_exchange(code)
        store.put(credentials)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # name=>offset
    # datetime.datetime.now(pytz.timezone('Europe/Prague')).strftime('%z')

    calendars_list = service.calendarList().list().execute().get('items', [])
    print('Calendars list')
    for calendar in calendars_list:
        print('Id: ', calendar['id'], '|', calendar['summary'], '|', calendar['timeZone'])

    #print(calendars_list)
    print('Getting today events from primary calendar')
    tz = '+0100'
    time_zone = datetime.timedelta(hours=int(tz[0:3]), minutes=int(tz[0]+tz[3:5]))
    h24 = datetime.timedelta(hours=8)
    #current_time = datetime.datetime.utcnow()
    start_time = datetime.datetime(2017, 12, 10, 0, 30, 0)
    end_time = datetime.datetime(2017, 12, 10, 10, 0, 0)
    # apply timeZone difference between utc and local time and convert to ISO-8601 datetime
    # timeMin = (current_time + time_zone).strftime("%Y-%m-%dT00:00:00"+tz)
    # timeMax = (current_time + time_zone).strftime("%Y-%m-%dT23:59:59"+tz)
    timeMin = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    timeMax = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(timeMin, timeMax)
    eventsResult = service.events().list(
        calendarId='primary', timeMin=timeMin, timeMax=timeMax, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    #print(eventsResult)
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        #print(event)
        #print(json.dumps(event))
        # Normal event will have start.dateTime, allday event => start.date
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print(start,'|', event['summary'],'|', end)


if __name__ == '__main__':
    main()
