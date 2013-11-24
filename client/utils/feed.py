#!/usr/bin/env python

import sys
sys.path.insert(0, '.')

import requests
import json
from models import Pinche
from requests.auth import HTTPBasicAuth
    
def test_get():
    r = requests.get("http://127.0.0.1:5000/api/oursnews/1/")
    print r.json

# def test_post(auth):
#     payload = {'txt': 'hahaha'}
#     r = requests.post("http://127.0.0.1:5000/api/oursnews/", data=json.dumps(payload), auth=auth)
#     return r.json["id"]

# def test_put(auth, pinche_id):
#     payload = {'txt': 'hahaha'}
#     r = requests.put("http://127.0.0.1:5000/api/oursnews/%s/" %(oursnews_id), data=json.dumps(payload), auth=auth, )
#     print r.json

def test_delete(auth, pinche_id):
    r = requests.delete("http://127.0.0.1:5000/api/oursnews/%s/" %(oursnews_id), auth=auth)
    print r.json
    
if __name__ == "__main__":
    auth=HTTPBasicAuth('admin', 'admin')
    # host_id = test_post(auth)
    # test_put(auth, host_id )
    test_get()
    # test_delete(auth, host_id)
    # test_get()
