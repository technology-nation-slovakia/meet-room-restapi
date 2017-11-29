from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from flask import jsonify
#from cs50 import SQL

import cs50
#from app.google.sql2 import SQL

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # home_dir = os.path.expanduser('~')
    # credential_dir = os.path.join(home_dir, '.credentials')
    # if not os.path.exists(credential_dir):
    #     os.makedirs(credential_dir)
    credential_path = os.path.join(os.getcwd(),
                                   'calendar-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES,redirect_uri='http://localhost') #predtym mi otovirlo textovy webovy prehliadac Linuxu, cez ktory som sa nevedel prihlasit
        flow.user_agent = APPLICATION_NAME
        auth_uri = flow.step1_get_authorize_url()
        print("Open foolowing url in browser: ",auth_uri)
        code = input('Input code: ')
        credentials = flow.step2_exchange(code)
        store.put(credentials)

        # if flags:
        #     credentials = tools.run_flow(flow, store, flags)
        # else: # Needed only for compatibility with Python 2.6
        #     credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main(room):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    #now = datetime.datetime.utcnow().isoformat()  + 'Z' # 'Z' indicates UTC time
    timeMin = datetime.datetime.utcnow().strftime("%Y-%m-%dT00:00:00.%f" + 'Z')
    timeMax = datetime.datetime.utcnow().strftime("%Y-%m-%dT23:59:59.%f" + 'Z')

    #print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId=room['id_remote'], timeMin=timeMin, timeMax=timeMax, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    #if not events:
        #print('No upcoming events found.')

    #db = SQL("sqlite:///calendar.db")

    for event in events:
        #print(event, type(event))
        #start = event['start'].get('dateTime', event['start'].get('date'))
        #end = event['end'].get('dateTime', event['end'].get('date'))
        #organizer = event['organizer'].get('email', event['organizer'].get('email'))
        #creator = event['creator'].get('email', event['creator'].get('email'))

        #deal with the situation, when user does not fill in the calendar description, summary, visibility - stays default
        visibility = "FALSE"
        try:
            description = event['description']
            summary = event['summary']
            if event['visibility'] == "private":
                visibility = "TRUE"
        except KeyError:
            description = ""
            summary = ""
            visibility = "FALSE"

        #print(start, summary, end)

        # result = db.execute("INSERT into Items (user_id, event_id, event_org, event_creat, event_name, event_descript, start_date, end_date, isPrivate, place_id, item_type_id, parent_id) VALUES (:user_id, :event_id, :event_org, :event_creat, :event_name, :event_descript, :start_date, :end_date, :isPrivate, :place_id, :item_type_id, :parent_id)",
        #     user_id = 1,
        #     event_id = event['id'],
        #     event_org = organizer,
        #     event_creat = creator,
        #     event_name = summary,
        #     event_descript = description,
        #     start_date = start,
        #     end_date = end,
        #     isPrivate = visibility,
        #     place_id = 1,
        #     item_type_id = 1,
        #     parent_id = 1)

    return events


if __name__ == '__main__':
    main()
