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
    news_list = OursNews.select().order_by('score')
    return object_list('index.html', news_list, "news_list")

@app.route('/ournews/<int:news_id>/')
def news_detail(news_id):
    obj = get_object_or_404(OursNews, id=news_id)
    return render_template('news_detail.html', obj=obj)
    