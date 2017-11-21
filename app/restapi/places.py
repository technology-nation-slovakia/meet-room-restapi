# version 0.1.0

from flask_restful import Resource
from app.sql import runSQL
from datetime import datetime


# Places RESTful endpoint methods definition
class Places(Resource):
    def get(self,  place_id=None, item_id=None, startDate=None, endDate=None):
        if startDate:
            # extract date from the startDate string
            startDate1 = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S').date()
            return runSQL('''

                SELECT * FROM (

                    SELECT id as item_id, name as item_name, description, start_date, end_date, isPrivate, place_ID as places_id, itemtype_ID as item_type_id
                    FROM items
                    WHERE
                    place_ID = {1}
                    AND itemtype_ID = 1
                    AND datetime(start_date) <= '{0}'
                    AND datetime(end_date) > '{0}'

                    UNION ALL

                    SELECT NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL /*if there is no ongoing event return array of NULLs*/

                    LIMIT 1
                    )

                UNION ALL

                SELECT * FROM (

                    SELECT * FROM (

                        SELECT id as item_id, name as item_name, description, start_date, end_date, isPrivate, place_ID as places_id, itemtype_ID as item_type_id
                        FROM items
                        WHERE
                        place_ID = {1}
                        AND itemtype_ID = 1
                        AND datetime(start_date) > '{0}'
                        AND date(end_date) = '{2}'
                        ORDER BY start_date
                        LIMIT 1
                        )

                    UNION ALL

                    SELECT NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL /*if there is no upcoming event to the end of the actual day return array of NULLs*/

                    LIMIT 1
                    )
                ;
                '''.format(startDate, place_id, startDate1)), 200

        elif place_id:
            return runSQL('''
                SELECT id as item_id, name as item_name, description, start_date, end_date, isPrivate, place_ID as places_id, itemtype_ID as item_type_id
                FROM items
                WHERE place_ID = {};
                '''.format(place_id)), 200 # HTTP status code 200 OK


        else:
            return runSQL('''
                SELECT id as item_id, name as item_name, description, start_date, end_date, isPrivate, place_ID as places_id, itemtype_ID as item_type_id
                FROM items;
                '''), 200

    def post(self, id=None):
        return {'places': 'Add new place'}

    # PUT method
    def put(self, id=None):
        if id:
            return {'places': 'update place id={}'.format(id)}, 200
        else:
            return {'places': 'Update failed'}, 400 # Bad Request


    def delete(self, id=None):
        if id:
            return {'places': 'delete place id={}'.format(id)}, 200
        else:
            return {'places': 'delete all places'}, 200