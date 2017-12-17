# Places RESTful endpoints
from flask_restful import Resource
from app.sql import runSQL
from app.google_calendar import gc_sync_db, gc_synced
from app import app

class Places(Resource):
    def get(self,  place_id=None):
        if place_id:
            return runSQL('''
                SELECT *
                FROM places
                WHERE id={};
                '''.format(place_id)), 200 # HTTP status code 200 OK
        else:
            return runSQL('''
                SELECT *
                FROM places;
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


class PlacesItems(Resource):
    def get(self, place_id, start_date=None, end_date=None):

        if end_date:
            gc_sync_db(place_id, start_date, end_date)
            return runSQL('''
                SELECT {fields}
                FROM items
                WHERE place_id = {place_id}
                AND ((datetime(start_date) < datetime('{start_date}') AND datetime('{start_date}') < datetime(end_date))
                    OR (datetime('{start_date}') <= datetime(start_date) AND datetime(end_date) <= datetime('{end_date}'))
                    OR (datetime(start_date) < datetime('{end_date}') AND datetime('{end_date}') < datetime(end_date)));
                '''.format(place_id=place_id, start_date=start_date, end_date=end_date, fields=app.config['SQL_DEFAULT_FIELDS'])), 200
        elif start_date:
            gc_sync_db(place_id, start_date)
            return runSQL('''
                SELECT {fields}
                FROM items
                WHERE place_id = {place_id}
                AND ((datetime(start_date) < datetime('{start_date}') AND datetime('{start_date}') < datetime(end_date))
                    OR (datetime('{start_date}') <= datetime(start_date) AND datetime(end_date) <= datetime(datetime('{start_date}'),'+24 hours'))
                    OR (datetime(start_date) < datetime(datetime('{start_date}'),'+24 hours') AND datetime(datetime('{start_date}'),'+24 hours') < datetime(end_date)));
                '''.format(place_id=place_id, start_date=start_date, fields=app.config['SQL_DEFAULT_FIELDS'])), 200

        else:
            return runSQL('''
                SELECT {fields}
                FROM items
                WHERE place_id = {place_id};
                '''.format(place_id=place_id, fields=app.config['SQL_DEFAULT_FIELDS'])), 200 # HTTP status code 200 OK


class PlacesItemsNow(Resource):
    def get(self, place_id):
        if not gc_synced():
            gc_sync_db()
        # ongoing event
        a = runSQL('''
            SELECT {fields}
            FROM items
            WHERE place_id={place_id}
                AND itemtype_id=1
                AND datetime(start_date) <= datetime('now')
                AND datetime('now') <= datetime(end_date)
                ORDER BY id_remote DESC, start_date
                LIMIT 1;
                '''.format(place_id=place_id, fields=app.config['SQL_DEFAULT_FIELDS']))

        # upcoming event
        b = runSQL('''
            SELECT {fields}
            FROM items
            WHERE place_id={place_id}
            AND itemtype_id=1
            AND datetime(start_date) > datetime('now')
            AND date(start_date) = date('now')
            ORDER BY id_remote DESC, start_date
            LIMIT 1;
                '''.format(place_id=place_id, fields=app.config['SQL_DEFAULT_FIELDS']))

        c = []
        #if a or b:
        c.append(a)
        c.append(b)

        return c, 200



