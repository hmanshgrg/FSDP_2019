# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:01:08 2019

@author: Amisha Garg
"""



import pymongo
client = pymongo.MongoClient("mongodb+srv://hmansh:himanshu@cluster0-gomlk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db1=client.hmansh
def add_records(rollno, name, age, branch):
    db1.yourcollectionname.insert_one(
            {
            "Roll":rollno,
            "Name":name,
            "Age":age,
            "Branch":branch
            })
    return "Record entered successfully"
def fetch_all_records():
    user =db1.yourcollectionname.find()
    for i in user:
        print (i)
add_records(1,'Himanshu',20,'cse')
add_records(2,'Hemant',30,'cse')
add_records(3,'Ankush',19,'cse')
add_records(4,'Ashu',21,'cse')
add_records(5,'Gupta',22,'cse')

fetch_all_records()