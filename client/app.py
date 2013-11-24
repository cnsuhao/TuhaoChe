from flask import Flask

# flask-peewee bindings
from flask_peewee.db import Database


app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    from models import User, News, OursNews

    # User.create_table()
    
    News.create_table()
    OursNews.create_table()