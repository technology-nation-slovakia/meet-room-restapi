# Google Calendar RESTful endpoint
from flask_restful import Resource
from app.sql import runSQL
from app.google_calendar import gc_today_events


# Places  methods definition
class PlacesGoogleEvents(Resource):
    def get(self,  place_id=None):
        if place_id:
            room = runSQL('''
                SELECT *
                FROM places
                WHERE ID = {};
                '''.format(place_id))

            if room: # get events from Google Calendar
                events = gc_today_events(room['id_remote'])
            else:
                events = {}

            if events is not None:
                return events, 200
            else:
                return "Google Calendar API error", 403 #403 FORBIDDEN



