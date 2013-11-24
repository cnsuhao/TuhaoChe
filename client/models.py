#!/bin/python
#coding: utf-8

from hashlib import md5, sha1
import datetime

from flask_peewee.auth import BaseUser

from peewee import *

from app import app,db

 # "created_at" : "Mon Nov 29 16:08:43 +0800 2010",
# "text" : "各位开发者，我们的论坛上线啦~http://sinaurl.cn/h4FWc7 欢迎大家的参与~另外，关于技术相关的问题，可以在论坛上提出，也可以@微博API 这个官方技术支持账号哦~感谢大家对开放平台的支持~[呵呵]",
# "truncated" : false,
# "in_reply_to_status_id" : "",
# "in_reply_to_screen_name" : "",
# "geo" : null,
# "user" : 
# {
# "name" : "微博开放平台",
# "domain" : "openapi",
# "geo_enabled" : true,
# "followers_count" : 13034,
# "statuses_count" : 157,
# "favourites_count" : 0,
# "city" : "8",
# "description" : "新浪微博开放平台市场推广官方账号，如有技术问题，请@微博API或者发私信给微博API",
# "verified" : true,
# "id" : 11051,
# "gender" : "m",
# "friends_count" : 5,
# "screen_name" : "微博开放平台",
# "allow_all_act_msg" : true,
# "following" : false,
# "url" : "http://open.t.sina.com.cn/",
# "profile_image_url" : "http://tp4.sinaimg.cn/11051/50/1280283165/1",
# "created_at" : "Wed Jan 20 00:00:00 +0800 2010",
# "province" : "11",
# "location" : "北京 海淀区"
# },
# "favorited" : false,
# "in_reply_to_user_id" : "",
# "id" : 3958728723,
# "source" : "<a href=\"http://t.sina.com.cn\" rel=\"nofollow\">新浪微博</a>"

class User(db.Model, BaseUser):
    # followers_count = IntegerField()
    # statuses_count = IntegerField()
    # favourites_count = IntegerField()
    username = CharField()
    
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
   
# 
# class User(db.Model, BaseUser):
#     username = CharField()
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField(default=datetime.datetime.now)
#     active = BooleanField(default=True)
#     admin = BooleanField(default=False)
#     
#     def __unicode__(self):
#         return self.username
# 
#     def following(self):
#         return User.select().join(
#             Relationship, on='to_user_id'
#         ).where(from_user=self).order_by('username')
# 
#     def followers(self):
#         return User.select().join(
#             Relationship, on='from_user_id'
#         ).where(to_user=self).order_by('username')
# 
#     def is_following(self, user):
#         return Relationship.filter(
#             from_user=self,
#             to_user=user
#         ).exists()
# 
#     def gravatar_url(self, size=80):
#         return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
#             (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)
# 
# class Relationship(db.Model):
#     from_user = ForeignKeyField(User, related_name='relationships')
#     to_user = ForeignKeyField(User, related_name='related_to')
# 
#     def __unicode__(self):
#         return 'Relationship from %s to %s' % (self.from_user, self.to_user)
# 
# class Message(db.Model):
#     user = ForeignKeyField(User)
#     content = TextField()
#     pub_date = DateTimeField(default=datetime.datetime.now)
# 
#     def __unicode__(self):
#         return '%s: %s' % (self.user, self.content)
# 
# class Note(db.Model):
#     user = ForeignKeyField(User)
#     message = TextField()
#     status = IntegerField(choices=((1, 'live'), (2, 'deleted')), null=True)
#     created_date = DateTimeField(default=datetime.datetime.now)
# 
# class City(db.Model):
#     name = CharField()
# 
#     def __unicode__(self):
#         return self.name
#     
# class Pinche(db.Model):
#     city = ForeignKeyField(City)
#     title = CharField()
#     car = CharField();
#     time = CharField()
#     phone = CharField()
#     route = CharField()
#     publisher = CharField()
#     content = TextField()
#     pub_date = DateTimeField(default=datetime.datetime.now)
# 
# class CarBrand(db.Model):
#     name = CharField()
# 
#     def __unicode__(self):
#         return self.name
# 
# class CarSeries(db.Model):
#     brand = ForeignKeyField(CarBrand)
#     name = CharField()
# 
#     def __unicode__(self):
#         return self.name
# 
# class CarModel(db.Model):
#     series = ForeignKeyField(CarSeries)
#     name = CharField()
# 
#     def __unicode__(self):
#         return self.name
    