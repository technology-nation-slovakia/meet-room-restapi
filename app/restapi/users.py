# Users RESTful endpoints

from flask_restful import Resource

class Users(Resource):
    # GET method
    def get(self, id=None):
        if id:
            print('id=', id)
            return {'users': 'User details id={}'.format(id)}, 200 # OK
        else:
            return {'users': 'List all users'}, 200

    # POST method
    def post(self, id=None):
        return {'users': 'Add new User'}

    # PUT method
    def put(self, id=None):
        if id:
            return {'users': 'Update User info id={}'.format(id)}, 200
        else:
            return {'users': 'Update failed. No id'}, 400 # Bad Request

    # DELETE method
    def delete(self, id=None):
        if id:
            return {'users': 'delete User id={}'.format(id)}, 200
        else:
            return {'users': 'delete all users'}, 200


class UserLogin(Resource):
    # GET method
    def post(self):
        return {'user': 'User login'}, 200

class UserLogout(Resource):
    # GET method
    def get(self):
        return {'user': 'User loged out'}, 200

class UserWhois(Resource):
    # GET method
    def get(self):
        return {'user': 'User whois'}, 200