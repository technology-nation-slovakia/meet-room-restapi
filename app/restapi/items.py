# Items module

from flask_restful import Resource
from app.sql import runSQL

# Items RESTful endpoint methods definition
class Items(Resource):
    # GET method
    def get(self, id = None, startDate = None, endDate = None):
        if id:
            return runSQL('''
                SELECT items.id as id, items.name as name, items.description as description, start_date, end_date, isPrivate,
                    users.id as user_id, users.name || ' ' || users.surname as user,
                    places.id as place_id, places.name as place,
                    item_type.id as type_id, item_type.name as type
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id
                AND items.id = {};
                '''.format(id)), 200 # HTTP status code 200 OK

        elif startDate:
            return runSQL('''
                SELECT items.id as id, items.name as name, items.description as description, start_date, end_date, isPrivate,
                    users.id as user_id, users.name || ' ' || users.surname as user,
                    places.id as place_id, places.name as place,
                    item_type.id as type_id, item_type.name as type
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id
                AND date(start_date) >= '{0}'
                AND date(end_date) <= '{1}';
                '''.format(startDate, endDate or startDate)), 200
        else:
            return runSQL('''
                SELECT items.id as id, items.name as name, items.description as description, start_date, end_date, isPrivate,
                    users.id as user_id, users.name || ' ' || users.surname as user,
                    places.id as place_id, places.name as place,
                    item_type.id as type_id, item_type.name as type
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id;
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