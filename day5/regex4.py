# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:00:16 2019

@author: Amisha Garg
"""

import re
lt=[]
email=input("Enter email ").split(" ")
for i in email:
    res=re.findall(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',i)
    for j in res:
        lt.append(j)
print(lt)