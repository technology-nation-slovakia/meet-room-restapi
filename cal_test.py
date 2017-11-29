from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from flask import jsonify

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

    eventsResult = service.events().list(
        calendarId=room['id_remote'], timeMin=timeMin, timeMax=timeMax, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    for event in events:
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

    return events

if __name__ == '__main__':
    main()
