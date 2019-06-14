# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:15:07 2019

@author: Amisha Garg
"""

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
lt=[]
for i in orders:
    x=i[2]*i[3]
    if(x<100):
        t=(i[0],round((x+10),2))
        lt.append(t)
    else:
        t=(i[0],x)
        lt.append(t)
print(lt)        







########################################################

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]

lt=list(map(lambda x: x[0],orders))
lt1=list(map(lambda x:(x[2]*x[3])+10 if x[2]*x[3]<100 else x[2]*x[3],orders))
res1=list(zip(lt,lt1,))
print(res1)



























