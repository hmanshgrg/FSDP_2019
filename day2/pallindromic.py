# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:09:52 2019

@author: Amisha Garg
"""

n=input("Enter no's ").split()

print(n)
s ,c=0 ,0
for i in n:
    x=int(i)
    i=int(i)
    
    while (i>0):
        a=int(i%10)
        s=int(s*10+a)
        i=int(i/10)
    if s==x:
       c=1
if c==1:
    print("True")
else:
    print("False")