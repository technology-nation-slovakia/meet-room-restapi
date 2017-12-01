# Google Calendar module
from flask_restful import Resource
from app.sql import runSQL
from app.google_calendar import today_events
import datetime

# Places RESTful endpoint methods definition
class PlacesGoogleEvents(Resource):
    def get(self,  place_id = None):
        if place_id:
            room = runSQL('''
                SELECT *
                FROM places
                WHERE ID = {};
                '''.format(place_id))

            if room: # get events from Google Calendar

                events = today_events(room['id_remote'], room['timeZone'])

                timeZone = datetime.timedelta(hours = room['timeZone'])
                currentTime = datetime.datetime.utcnow()
                time = timeZone + currentTime

                updated_default = 0

                SetUpdatedToZero = runSQL('''
                                   UPDATE Items SET updated = '{0}'
                                   WHERE date(start_date) = date('{1}')
                                   AND place_id = '{2}';
                                   '''.format(updated_default, time, place_id))

                for event in events:
                    user_id = 1
                    itemtype_id = 1
                    updated = 1
                    visibility = "FALSE"
                    #when event description is no set - missing
                    try:
                        description = event['description']
                    except KeyError:
                        description = ""
                    #when event name is no set - missing
                    try:
                        summary = event['summary']
                    except KeyError:
                        summary = ""
                    #when event visibility is set by default
                    try:
                        if event['visibility'] == "private":
                            visibility = "TRUE"
                    except KeyError:
                        visibility = "FALSE"

                    CheckIfEventExistInDb = runSQL('''
                        SELECT id_remote
                        FROM Items
                        WHERE id_remote = '{0}'
                        AND place_id = '{1}';
                        '''.format(event["id"], place_id))
                    #user can change the room of already created event, the id stays in this case the same
                    if not CheckIfEventExistInDb:
                        insert = runSQL('''INSERT INTO Items (name, description, start_date, end_date, isPrivate, user_id, place_id, itemtype_id, id_remote, updated)
                            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}');
                            '''.format(summary,description,event["start"]["dateTime"],event["end"]["dateTime"], visibility, user_id, place_id, itemtype_id, event["id"], updated))

                    else:
                        update = runSQL('''UPDATE Items SET name = '{0}', description = '{1}', start_date = '{2}', end_date = '{3}', isPrivate = '{4}', user_id = '{5}', place_id = '{6}', itemtype_id = '{7}', updated = '{9}'
                            WHERE id_remote = '{8}'
                            AND place_id = '{6}';
                            '''.format(summary,description,event["start"]["dateTime"],event["end"]["dateTime"], visibility, user_id, place_id, itemtype_id, event["id"], updated))

                delete = runSQL('''
                    DELETE FROM Items
                    WHERE date(start_date) = date('{0}')
                    AND updated = '{1}'
                    AND place_id = '{2}';
                    '''.format(time, updated_default, place_id))


            else:
                events = {}

            if events is not None:
                return events, 200
            return "Google Calendar API error", 500



