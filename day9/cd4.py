# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:33:25 2019

@author: Amisha Garg
"""

from bs4 import BeautifulSoup as bs
import requests 
import sqlite3
from pandas import DataFrame
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(url).text
soup = bs(source,"lxml")
ptable=soup.find('table', class_='table')
A=[]
B=[]
C=[]
D=[]
for rows in ptable.findAll('tr'):
    cells=rows.findAll('td')
    if len(cells)==5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())
con=sqlite3.connect("ranking.db")
c=con.cursor()
c.execute("""CREATE TABLE rank(
        rank INTEGER,
        team_name TEXT,
        points INTEGER,
        rating INTEGER)""")
for i in range(0,16):
    c.execute("insert into rank values('{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i]))
c.execute("select * from rank")
df = DataFrame(c.fetchall())
df.columns = ["Rank","Team_name","Points","Rating"]
con.commit()
con.close()
c.execute("drop table rank")