from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, AdminAuthentication, RestrictOwnerResource

from app import app
from auth import auth

from models import User, News, OursNews

user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)

# instantiate our api wrapper
api = RestAPI(app, default_auth=user_auth)

class UserResource(RestResource):
     exclude = ()

class NewsResource(RestResource):
    exclude = ()

class OursNewsResource(RestResource):
    exclude = ()
    
api.register(User, UserResource, auth=admin_auth)
api.register(News, NewsResource)
api.register(OursNews, OursNewsResource)
