# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:23:55 2019

@author: Amisha Garg
"""

from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Amisha Garg\Downloads\chromedriver_win32\chromedriver.exe")
url="https://bidplus.gem.gov.in/bidlists"
driver.get(url)
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
for i in range(1,11):
    a.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    b.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    c.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    d.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    e.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    f.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)


from collections import OrderedDict

name = ["bid_no","Items","Quantity","Dept_name_add","S_date","E_date"]
data = OrderedDict(zip(name,[a,b,c,d,e,f]))
import pandas as pd
df = pd.DataFrame(data)

