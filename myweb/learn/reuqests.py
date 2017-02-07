__author__ = 'haosj'
#coding:utf-8
import requests
import json

url=r'http://127.0.0.1:8000/api/get_event_list/'
print url
r=requests.get(url,params={'eid':'1'})
result=r.json()['data']

print result['name']