# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:44:27 2019

@author: Amisha Garg
"""
import re
cc=input("Enter credit card no.").split(" ")
for i in cc:
    res=re.findall(r'[^[456][\d]{3}-[\d]{4}-[\d]{4}-[\d]{4}]|^[456][\d]{15}(\d)\1{3,}',i)
    if res:
        print("Valid")
    else:
        print("Not Valid")
        
        
        
        
        
