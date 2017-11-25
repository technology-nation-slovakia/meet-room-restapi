# Items module

from flask_restful import Resource
from app.sql import runSQL

# Items RESTful endpoint methods definition
class Items(Resource):
    # GET method
    def get(self, id = None, startDate = None, endDate = None):
        if id:
            return runSQL('''
                SELECT *
                FROM items
                WHERE items.id = {};
                '''.format(id)), 200 # HTTP status code 200 OK

        elif startDate:
            return runSQL('''
                SELECT *
                FROM items
                WHERE date(start_date) >= '{0}'
                AND date(end_date) <= '{1}';
                '''.format(startDate, endDate or startDate)), 200
        else:
            return runSQL('''
                SELECT *
                FROM items;
                '''), 200

    # POST method
    def post(self, id = None):
        return {'items': 'Add new item'}

    # PUT method
    def put(self, id = None):
        if id:
            return {'items': 'update item id={}'.format(id)}, 200
        else:
            return {'items': 'Update failed. Missed ID'}, 400 # Bad Request

    # DELETE method
    def delete(self, id = None):
        if id:
            return {'items': 'delete item id={}'.format(id)}, 200
        else:
            return {'items': 'delete all items'}, 200