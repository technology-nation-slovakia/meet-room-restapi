# Google Calendar module
from flask_restful import Resource
from app.sql import runSQL
from app.google_calendar import today_events


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
            else:
                events = {}

            if events is not None:
                return events, 200
            return "Google Calendar API error", 500



