# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:33:39 2019

@author: Amisha Garg
"""
dic1={}
with open("romeo.txt","rt") as file:
    
    for line in file:
        rd=line.split(" ")
        for item in rd:
            if item in dic1:
                dic1[item]+1
            else:
                dic1[item]==1
    print(dic1)
    
        