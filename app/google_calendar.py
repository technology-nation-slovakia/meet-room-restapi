# Google Calendar (GC) sync module
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime
import pytz

from app import app
from app.console_log import console_log
from app.sql import runSQL

def gc_get_credentials():
    store = Storage(app.config['GC_CLIENT_CREDENTIALS'])
    credentials = store.get()
    if not credentials or credentials.invalid:
        console_log('Missed or invalid Google Calendar API credentials', 'fail')
        return None
    return credentials

def gc_get_events(calendar_id, start_datetime, end_datetime):
    # read GC credentials. Return None if fail.
    credentials = gc_get_credentials()
    if not credentials:
        return None

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http = http)

    # Get calendars metadata
    console_log('Retrieve data from Google Calendar', 'info')
    calendar = service.calendars().get(calendarId=calendar_id).execute()
    # timezone name according to tz database
    tz_name = calendar['timeZone']
    # convert timezone name to utc offset in format ±HHMM
    tz_offset = datetime.datetime.now(pytz.timezone(tz_name)).strftime('%z')
    console_log('ID: {0}, timezone: {1}, offset: {2}'.format(calendar_id, tz_name, tz_offset), 'info')

    # convert timezone offset to timedelta
    tz_delta = datetime.timedelta(hours=int(tz_offset[0:3]), minutes=int(tz_offset[0] + tz_offset[3:5]))
    ## apply timezone difference between utc and local time and convert it to ISO-8601 datetime
    #time_min = (start_datetime + tz_delta).strftime("%Y-%m-%dT00:00:00" + tz_offset)
    #time_max = ((end_datetime or start_datetime) + tz_delta).strftime("%Y-%m-%dT23:59:59" + tz_offset)

    time_min = start_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    time_max = end_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    console_log('UTC datetime range {} - {}'.format(time_min, time_max), 'info')

    # request events from Google Calendar
    events_result = service.events().list(
        calendarId = calendar_id, timeMin = time_min, timeMax = time_max, singleEvents = True,
        orderBy = 'startTime',  timeZone='UTC').execute()
    events = events_result.get('items', [])
    console_log('Recieved {0} events'.format(len(events)), 'info')

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        console_log('{} | {} | {}'.format(start, event.get('summary','N/A'), end), 'note')

    return events

# Get today events from GC
def gc_today_events(calendar_id):
    current_time = datetime.datetime.utcnow()
    events = gc_get_events(calendar_id, current_time, current_time + datetime.timedelta(hours=24))
    return events


# check if GC is synced
def gc_synced():
    # check difference since last synchronization
    if  datetime.datetime.now() - app.config['GC_LAST_SYNC'] > app.config['GC_SYNC_INTERVAL']:
        console_log('GC unsynchronized', 'warning')
        app.config['GC_LAST_SYNC'] = datetime.datetime.utcnow()
        return False
    else:
        console_log('GC synchronized. Last sync: '+ app.config['GC_LAST_SYNC'].isoformat(), 'info')
        return True

# Synchronize Google Calendar and DB
def gc_sync_db(place_id=None, start_date=None, end_date=None):
    if place_id:
        places = []
        places.append(runSQL('SELECT * FROM places WHERE id={};'.format(place_id)))
    else:
        places = runSQL('SELECT * FROM places;')

    # if dates empty set time range [utc.now; utc.now+24H]
    if start_date:
        start_datetime = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    else:
        start_datetime = datetime.datetime.utcnow()

    if end_date:
        end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
    else:
        end_datetime = start_datetime + datetime.timedelta(hours=24)

    for place in places:
        events = gc_get_events(place['id_remote'], start_datetime, end_datetime)

        if place_id:
            # reset update flag for google calendars related items in time range [start_datetime;end_datetime]
            runSQL('''
                UPDATE items
                SET updated = 0
                WHERE id_remote
                AND place_id = {place_id}
                AND ((datetime(start_date) < datetime('{start_datetime}') AND datetime('{start_datetime}') < datetime(end_date))
                    OR (datetime('{start_datetime}') <= datetime(start_date) AND datetime(end_date) <= datetime('{end_datetime}'))
                    OR (datetime(start_date) < datetime('{end_datetime}') AND datetime('{end_datetime}') < datetime(end_date)));
                '''.format(place_id=place_id, start_datetime=start_datetime.strftime('%Y-%m-%dT%H:%M:%SZ'),
                            end_datetime=end_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')))

            for event in events:
                # try update existed event otherwise insert
                if runSQL('''
                    UPDATE items
                        SET name = '{name}',
                        description = '{desc}',
                        start_date = '{start_date}',
                        end_date = '{end_date}',
                        user_id = 1, updated = 1
                        WHERE place_id = {place_id}
                        AND id_remote = '{id_remote}';
                        '''.format(place_id=place_id, name=event.get('summary','N/A').strip(), desc=event.get('description', 'N/A').strip(),
                        start_date=datetime.datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                        end_date=datetime.datetime.strptime(event['end']['dateTime'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                        id_remote=event['id'])):
                    pass
                else:
                    runSQL('''
                        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id, id_remote, updated)
                        VALUES ('{name}','{desc}','{start_date}','{end_date}', 1, {place_id}, 1, '{id_remote}', 1);
                        '''.format(place_id=place_id, name=event.get('summary','N/A').strip(), desc=event.get('description','N/A').strip(),
                        start_date=datetime.datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                        end_date=datetime.datetime.strptime(event['end']['dateTime'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                        id_remote=event['id']))

            # remove not updated items
            runSQL('''
                DELETE FROM items where not updated;
                ''')