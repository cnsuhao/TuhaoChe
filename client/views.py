import datetime

from flask import request, redirect, url_for, render_template, flash

from flask_peewee.utils import get_object_or_404, object_list

from app import app
from auth import auth
from models import User, OursNews

@app.route('/')
def homepage():
    return public_timeline()

@app.route('/public/')
def public_timeline():
    news_list = OursNews.select().order_by(('created_at', 'desc'))
    return object_list('index.html', news_list, 'news_list')
