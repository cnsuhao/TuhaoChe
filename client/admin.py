import datetime
from flask import request, redirect

from flask_peewee.admin import Admin, ModelAdmin, AdminPanel
from flask_peewee.filters import QueryFilter

from app import app, db
from auth import auth
from models import User, News, OursNews

admin = Admin(app, auth)

class NewsAdmin(ModelAdmin):
    columns = ('user', 'text', 'favorited', 'thumbnail_pic', 'bmiddle_pic', 'original_pic', 'reposts_count', 'comments_count', 'attitudes_count',  'screen_name', 'name', 'profile_image_url', 'avatar_large', 'uid', 'ret_text', 'created_at', 'score')

class OursNewsAdmin(ModelAdmin):
    columns = ('user', 'text', 'favorited', 'thumbnail_pic', 'bmiddle_pic', 'original_pic', 'reposts_count', 'comments_count', 'attitudes_count',  'screen_name', 'name', 'profile_image_url', 'avatar_large', 'uid', 'ret_text', 'created_at', 'score')

# admin.register(User, UserAdmin)
admin.register(News, NewsAdmin)
admin.register(OursNews, OursNewsAdmin)
