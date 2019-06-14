# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:15:54 2019

@author: Amisha Garg
"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},{'name': 'Sam'}]
lt=reduce(lambda x,y:x+y,map(lambda y :y['height'],filter(lambda item:'height' in item,people)))
count_lt=len(list(filter(lambda item:'height' in item,people)))
avg = lt/count_lt
print("Average:"+str(avg))