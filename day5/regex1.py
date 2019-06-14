# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:35:50 2019

@author: Amisha Garg
"""
import re
da=input("Enter the number").split(",")
for i in da:
    res=re.findall(r'[+-]*[0-9]*\.[0-9]+',i)
    if res:
        print("True")
    else:
        print("false")



    