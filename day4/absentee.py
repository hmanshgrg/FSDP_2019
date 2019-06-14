# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:05:45 2019

@author: Amisha Garg
"""

with open ('absentee.txt','wt') as wf:
    s=0
    while s<=25:
        nm=input("Enter name")
        if not nm:
            break
        wf.write(nm+'\n')
        
   
with open ('absentee.txt','rt') as rf:
     data=rf.readlines()
     print(data)       