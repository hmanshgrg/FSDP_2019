# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:01:04 2019

@author: Amisha Garg
"""

import requests
url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=af017defd0ba57014156"
response=requests.get(url)
data=response.json()
print("conversion price :"+str(data["USD_INR"]))