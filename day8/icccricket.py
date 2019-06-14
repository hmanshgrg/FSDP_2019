# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:00:07 2019

@author: Amisha Garg
"""

from bs4 import BeautifulSoup as BS
import requests

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(url).text

soup = BS(source,"lxml")
ptable=soup.find('table', class_='table')
#print (ptable.prettify())
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

from collections import OrderedDict

name = ["Position","Team","Points","Rating"]
data = OrderedDict(zip(name,[A,B,C,D]))
import pandas as pd
df = pd.DataFrame(data) 
df.to_csv("ranking.csv",index=False)
    