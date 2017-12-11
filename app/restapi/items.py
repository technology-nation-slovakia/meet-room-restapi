# Items RESTful endpoints
from flask_restful import Resource
from app.sql import runSQL

class Items(Resource):
    # GET method
    def get(self, id=None, start_date=None, end_date=None):
        if id:
            return runSQL('''
                SELECT *
                FROM items
                WHERE items.id={};
                '''.format(id)), 200 # HTTP status code 200 OK

        elif start_date:
            return runSQL('''
                SELECT *
                FROM items
                WHERE date(start_date) >= '{0}'
                AND date(end_date) <= '{1}';
                '''.format(start_date, end_date or start_date)), 200
        else:
            return runSQL('''
                SELECT *
                FROM items;
                '''), 200

    # POST method
    def post(self, id=None):
        return {'items': 'Add new item'}

    # PUT method
    def put(self, id=None):
        if id:
            return {'items': 'update item id={}'.format(id)}, 200
        else:
            return {'items': 'Update failed. Missed ID'}, 400 # Bad Request

    # DELETE method
    def delete(self, id=None):
        if id:
            return {'items': 'delete item id={}'.format(id)}, 200
        else:
            return {'items': 'delete all items'}, 200


class ItemsNow(Resource):
    # GET method
    def get(self):
        return runSQL('''
            SELECT *
            FROM items
            WHERE start_date <= datetime('now')
                AND datetime('now') <= end_date
            ORDER BY start_date, place_id;
            '''.format(id)), 200 # HTTP status code 200 OK
