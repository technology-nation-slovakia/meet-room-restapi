# version 0.1.0

from flask_restful import Resource

# Places RESTful endpoint methods definition
class Places(Resource):
    def get(self,  id=None):
        if id:
            return {'places': 'Place details id={}'.format(id)}, 200 # OK
        else:
            return {'places': 'List all places'}, 200

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