# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:08:50 2019

@author: Amisha Garg
"""

n=input("Enter a list").split(" ")
l2= [int(x)>0 for x in [item[::-1]==item for item in n]]
print(all(l2))
