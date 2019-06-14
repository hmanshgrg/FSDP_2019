# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:18:28 2019

@author: Amisha Garg
"""
import requests
url="http://forsk.in/images/Forsk_logo_bw.png"
data=requests.get(url)
with open("Forsk_logo_bw.png",'wb') as img:
    img.write(data.content)