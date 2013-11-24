#!/usr/bin/env python

import sys
sys.path.insert(0, '.')

import requests
import json
from models import OursNews
from requests.auth import HTTPBasicAuth
    
def create_test_news(txt):
    return {
        'user': 1, 
        'text': txt, 
        'favorited': 'true',
        'thumbnail_pic': 'thumbnail_pic',
        'bmiddle_pic':  'bmiddle_pic', 
        'original_pic': 'original_pic', 
        'reposts_count': '10', 
        'comments_count': '30', 
        'attitudes_count': '5',  
        'screen_name': 'weibo',
        'name': 'weibo',
        'profile_image_url': 'profile_image_url',
        'avatar_large': 'avatar_large',
        'uid': 'uid', 
        'ret_text': 'ret_text', 
        'score': 10, 
    }
    
def test_get():
    r = requests.get("http://127.0.0.1:5000/api/oursnews/?ordering=score")
    print r.json
    r = requests.get("http://127.0.0.1:5000/api/oursnews/4/")
    print r.json
    
def test_post(auth):
    payload = create_test_news('old news')
    r = requests.post("http://127.0.0.1:5000/api/oursnews/", data=json.dumps(payload), auth=auth)
    return r.json["id"]

def test_put(auth, oursnews_id):
    payload = create_test_news('updated news')
    r = requests.put("http://127.0.0.1:5000/api/oursnews/%s/" %(oursnews_id), data=json.dumps(payload), auth=auth, )
    print r.json

def test_delete(auth, oursnews_id):
    r = requests.delete("http://127.0.0.1:5000/api/oursnews/%s/" %(oursnews_id), auth=auth)
    print r.json
    
if __name__ == "__main__":
    auth=HTTPBasicAuth('admin', 'admin')
    news_id = test_post(auth)
    test_put(auth, news_id )
    test_get()
    test_delete(auth, news_id)
    test_get()
    news_id = test_post(auth)
    print news_id
