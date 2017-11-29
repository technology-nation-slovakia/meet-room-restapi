# Places module
from flask_restful import Resource
from app.sql import runSQL
from app.google.cal_test import main


# Places RESTful endpoint methods definition
class GoogleEventsUpdate(Resource):
    def get(self,  place_id = None):
        if place_id:

            room = runSQL('''
                SELECT id_remote
                FROM places
                WHERE ID = {};
                '''.format(place_id))

            events = main(room)


            return events, 200



