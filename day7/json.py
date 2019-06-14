# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:33:43 2019

@author: Amisha Garg
"""

import requests

url= "http://api.openweathermap.org/data/2.5/weather?q=Udaipur&appid=e9185b28e9969fb7a300801eb026de9c"
print (url)
response = requests.get(url)
data=response.json()
for key, value in data.items():
    print (key, ":" ,value , "\n")


print("longitude:"+str(data["coord"]["lon"]))
print("latitude:"+str(data["coord"]["lat"]))
print("weather cond:"+str(data["weather"][0]["main"]))
print("wind speed:"+str(data["wind"]["speed"]))
print("Sunrise:"+str(data["sys"]["sunrise"]))
print("Sunset:"+str(data["sys"]["sunset"]))
