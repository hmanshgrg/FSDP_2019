# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:11:38 2019

@author: Amisha Garg
"""
import json
import requests
Host = "https://enolrplv5wuyo.x.pipedream.net/"

data ={"fname":"Himanshu","Lname":"Garg"}


headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )
