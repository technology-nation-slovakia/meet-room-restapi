# Places module
from flask_restful import Resource
from app.sql import runSQL


# Places RESTful endpoint methods definition
class Places(Resource):
    def get(self,  place_id = None):
        if place_id:
            return runSQL('''
                SELECT *
                FROM places
                WHERE ID = {};
                '''.format(place_id)), 200 # HTTP status code 200 OK
        else:
            return runSQL('''
                SELECT *
                FROM places;
                '''), 200

    def post(self, id = None):
        return {'places': 'Add new place'}

    # PUT method
    def put(self, id = None):
        if id:
            return {'places': 'update place id={}'.format(id)}, 200
        else:
            return {'places': 'Update failed'}, 400 # Bad Request


    def delete(self, id = None):
        if id:
            return {'places': 'delete place id={}'.format(id)}, 200
        else:
            return {'places': 'delete all places'}, 200


class PlacesItems(Resource):
    def get(self, place_id = None, startDate = None, endDate = None):
        if startDate:
            return runSQL('''
                SELECT *
                FROM items
                WHERE date(start_date) >= '{0}'
                AND date(end_date) <= '{1}'
                AND place_ID = {2};
                '''.format(startDate, endDate or startDate, place_id)), 200

        elif place_id:
            return runSQL('''
                SELECT *
                FROM items
                WHERE place_ID = {};
                '''.format(place_id)), 200 # HTTP status code 200 OK


class PlacesItemsNow(Resource):
    def get(self,  place_id = None):
        if place_id:
            # ongoing event
            a = runSQL('''
                SELECT *
                FROM items
                WHERE place_ID = {}
                    AND itemtype_ID = 1
                    AND start_date <= datetime('now')
                    AND datetime('now') <= end_date
                    ORDER BY start_date
                    LIMIT 1;
                    '''.format(place_id))

            # upcoming event
            b = runSQL('''
                SELECT *
                    FROM items
                    WHERE place_ID = {0}
                    AND itemtype_ID = 1
                    AND start_date > datetime('now')
                    AND date(start_date) = date('now')
                    ORDER BY start_date
                    LIMIT 1;
                    '''.format(place_id))

            c = []
            if a or b:
                c.append(a)
                c.append(b)

            return c, 200



