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
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
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
