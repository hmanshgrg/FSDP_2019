# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:19:00 2019

@author: Amisha Garg
"""

import re
lt=[]
with open("simpsons_phone_book.txt","rt") as rf:
    for line in rf:
        res=re.findall(r'J.*Neu',line)
        lt.append(res)
print(lt)









