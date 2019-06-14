# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:10:14 2019

@author: Amisha Garg
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
res=list(map(lambda x:random.choice(code_names),names))
print(res)
