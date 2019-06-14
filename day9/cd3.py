# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:25:39 2019

@author: Amisha Garg
"""

import mysql.connector 
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Amisha Garg\Downloads\chromedriver_win32\chromedriver.exe")
url="https://bidplus.gem.gov.in/bidlists"
driver.get(url)
conn = mysql.connector.connect(user='hmansh', password='hmansh244@',host='db4free.net', database = 'hmansh1')
c = conn.cursor()
c.execute("drop table bid")
c.execute ("""CREATE TABLE bid(
             bid_no TEXT,
             items TEXT,
             quantity INTEGER,
             dept TEXT,
             s_date TEXT,
             e_date TEXT
          )""")
conn.commit()
a=[]
b=[]
c1=[]
d=[]
e=[]
f=[]
for i in range(1,11):
    a.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    b.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    c1.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    d.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    e.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    f.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)
for i in range(0,10): 
    c.execute("insert into bid values('{}','{}',{},'{}','{}','{}')".format(a[i],b[i],c1[i],d[i],e[i],f[i]))
    conn.commit()
c.ececute("select * from bid")
c.fetchall()