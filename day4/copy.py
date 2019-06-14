# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:49:59 2019

@author: Amisha Garg
"""
file1 = open('new.txt','wt')
with open('words.txt','rt') as file:
    file_content = file.readlines()
file1.writelines(file_content)
file1.close()  
    