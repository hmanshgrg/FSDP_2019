# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:56:02 2019

@author: Amisha Garg
"""

nm=input("Enter file name")
try:
    file = open(nm +str('.txt'),  "rt" )
    print (file.name)
    lines=file.read().splitlines()
    last=lines[-1]
    print(last)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    file.close() 

