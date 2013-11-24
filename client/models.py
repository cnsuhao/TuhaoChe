#!/bin/python
#coding: utf-8

from hashlib import md5, sha1
import datetime

from flask_peewee.auth import BaseUser

from peewee import *

from app import app,db

class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    
    def __unicode__(self):
        return self.username

    def following(self):
        return User.select().join(
            Relationship, on='to_user_id'
        ).where(from_user=self).order_by('username')

    def followers(self):
        return User.select().join(
            Relationship, on='from_user_id'
        ).where(to_user=self).order_by('username')

    def is_following(self, user):
        return Relationship.filter(
            from_user=self,
            to_user=user
        ).exists()

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)
    
class News(db.Model):
    user = ForeignKeyField(User)
    text = TextField()
    # id=,
    favorited  = CharField()
    thumbnail_pic  = CharField()
    bmiddle_pic = CharField()
    original_pic  = CharField()
    reposts_count = CharField()
    comments_count = CharField()
    attitudes_count = CharField()
    # -------user----------
    screen_name  = CharField()
    name  = CharField()
    profile_image_url  = CharField()
    avatar_large = CharField()
    uid = CharField()
    ret_text = CharField()
    # ---------------------
    created_at = DateTimeField(default=datetime.datetime.now)
  
     
class OursNews(db.Model):
   user = ForeignKeyField(User)
   text = TextField()
   # id=,
   favorited  = CharField()
   thumbnail_pic  = CharField()
   bmiddle_pic = CharField()
   original_pic  = CharField()
   reposts_count = CharField()
   comments_count = CharField()
   attitudes_count = CharField()
   # -------user----------
   screen_name  = CharField()
   name  = CharField()
   profile_image_url  = CharField()
   avatar_large = CharField()
   uid = CharField()
   ret_text = CharField()
   # ---------------------
   created_at = DateTimeField(default=datetime.datetime.now)
