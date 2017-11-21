# API Module
from app import app
from flask_restful import Api

# RESTful API endpoints
from .restapi.items import Items
from .restapi.places import Places
#from .restapi.users import Users, UserLogin, UserLogout, UserWhois

api = Api(app)

# Add endpoints
api.add_resource(Items, '/api/items',
                        '/api/items/<string:id>',
                        '/api/items/dates/<string:startDate>',
                        '/api/items/dates/<string:startDate>/<string:endDate>')

api.add_resource(Places, '/api/places',
                         '/api/places/<string:place_id>/items',
                         '/api/places/<string:place_id>/items/now',
                         '/api/places/<string:place_id>/items/now/<string:startDate>')
# api.add_resource(Users, '/api/users', '/api/users/<string:id>')
# api.add_resource(UserLogin, '/api/user/login')
# api.add_resource(UserLogout, '/api/user/logout')
# api.add_resource(UserWhois, '/api/user/whois')
