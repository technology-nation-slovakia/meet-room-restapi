# Places module
from flask_restful import Resource
from app.sql import runSQL
from cal_test import main


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

            #a = runSQL('''UPDATE Items SET updated = 1 WHERE date(start_date) = date('now')''')

            #for event in events:
            #    b = runSQL('''INSERT INTO Items (name, description) VALUES ( {0}, {1});'''.format(event['name'], event['description']))
            #   b = runSQL('''SELECT * FROM Items WHERE id_remote = {};'''.format(event['id']))
            #   print(b)



            return events, 200



