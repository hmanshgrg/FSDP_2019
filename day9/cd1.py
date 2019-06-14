# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:56:00 2019

@author: Amisha Garg
"""


import sqlite3
from pandas import DataFrame

con=sqlite3.connect("db_university1")
c=con.cursor()

c.execute("""CREATE TABLE records(
        rollno INTEGER,
        name TEXT,
        age INTEGER,
        branch TEXT)""")
c.execute("INSERT INTO records VALUES(1,'Himanshu',20,'cse')")
c.execute("INSERT INTO records VALUES(2,'Hemant',30,'cse')")
c.execute("INSERT INTO records VALUES(3,'Ankush',19,'cse')")
c.execute("INSERT INTO records VALUES(4,'Ashu',21,'cse')")
c.execute("INSERT INTO records VALUES(5,'Gupta',22,'cse')")
c.execute("INSERT INTO records VALUES(6,'Harsh',18,'cse')")
c.execute("INSERT INTO records VALUES(7,'Him',12,'cse')")
c.execute("INSERT INTO records VALUES(8,'Himan',25,'cse')")
c.execute("INSERT INTO records VALUES(9,'Hima',2,'cse')")
c.execute("INSERT INTO records VALUES(10,'Deepak',10,'cse')")
c.execute("select * from records")
df = DataFrame(c.fetchall())
df.columns = ["rollno","Sname","Age","Branch"]
con.commit()
con.close()