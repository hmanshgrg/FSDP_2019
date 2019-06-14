# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:36:05 2019

@author: Amisha Garg
"""
dict1={}
s=0
w=0
c=0
with open("romeo.txt","rt") as rf:
    for line in rf:
        s=s+1
        rd=line.split(" ")
        for i in rd:
            w=w+1
            for j in i:
                c=c+1
    print ("lines="+str(s))
    print ("words="+str(w))
    print ("char="+str(c))