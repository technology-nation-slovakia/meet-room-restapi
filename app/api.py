# API Module
from app import app
from flask_restful import Api

# RESTful API endpoints
from . restapi.items import Items, ItemsNow
from . restapi.places import Places, PlacesItems, PlacesItemsNow
from . restapi.google import GoogleEventsUpdate
#from . restapi.users import Users, UserLogin, UserLogout, UserWhois

api = Api(app)

# Add endpoints
api.add_resource(Items,
                '/api/items',
                '/api/items/<string:id>',
                '/api/items/dates/<string:startDate>',
                '/api/items/dates/<string:startDate>/<string:endDate>')

api.add_resource(ItemsNow,
                '/api/items/now')

api.add_resource(Places,
                '/api/places',
                '/api/places/<string:place_id>')

api.add_resource(PlacesItems,
                '/api/places/<string:place_id>/items',
                '/api/places/<string:place_id>/items/dates/<string:startDate>',
                '/api/places/<string:place_id>/items/dates/<string:startDate>/<string:endDate>')

api.add_resource(PlacesItemsNow,
                '/api/places/<string:place_id>/items/now')

api.add_resource(GoogleEventsUpdate,
                '/api/google/<string:place_id>/items/now')

# api.add_resource(Users, '/api/users', '/api/users/<string:id>')
# api.add_resource(UserLogin, '/api/user/login')
# api.add_resource(UserLogout, '/api/user/logout')
# api.add_resource(UserWhois, '/api/user/whois')
