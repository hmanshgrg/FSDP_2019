# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:18:45 2019

@author: Amisha Garg
"""

names = ['Mary', 'Isla', 'Sam']
res=list(map(lambda i:hash(i),names))
print(res)