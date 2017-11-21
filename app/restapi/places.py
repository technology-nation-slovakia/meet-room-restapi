# version 0.1.0

from flask_restful import Resource
from app.sql import runSQL

# Places RESTful endpoint methods definition
class Places(Resource):
    def get(self,  place_id=None, item_id=None, startDate=None, endDate=None):
        if startDate:
            return runSQL('''
                SELECT places.id as place_id, places.name as place_name, items.id as item_id, items.name as item_name, items.description as description, start_date, end_date, isPrivate,
                    item_type.id as type_id, item_type.name as type,
                    users.id as user_id, users.name || ' ' || users.surname as user
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id
                AND date(start_date) >= '{0}'
                AND date(end_date) <= '{1}'
                AND places.id = {2};
                '''.format(startDate, endDate or startDate, place_id)), 200

        elif item_id:
            return runSQL('''
                SELECT places.id as place_id, places.name as place_name, items.id as item_id, items.name as item_name, items.description as description, start_date, end_date, isPrivate,
                    item_type.id as type_id, item_type.name as type,
                    users.id as user_id, users.name || ' ' || users.surname as user
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id
                AND places.id = {0}
                AND items.id = {1};
                '''.format(place_id, item_id)), 200

        elif place_id:
            return runSQL('''
                SELECT places.id as place_id, places.name as place_name, items.id as item_id, items.name as item_name, items.description as description, start_date, end_date, isPrivate,
                    item_type.id as type_id, item_type.name as type,
                    users.id as user_id, users.name || ' ' || users.surname as user
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id
                AND places.id = {};
                '''.format(place_id)), 200 # HTTP status code 200 OK

        else:
            return runSQL('''
                SELECT places.id as place_id, places.name as place_name, items.id as item_id, items.name as item_name, items.description as description, start_date, end_date, isPrivate,
                    item_type.id as type_id, item_type.name as type,
                    users.id as user_id, users.name || ' ' || users.surname as user
                FROM items, users, places, item_type
                WHERE items.user_id = users.id
                AND items.place_id = places.id
                AND items.itemtype_id = item_type.id;
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