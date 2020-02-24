#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:07:21 2019

@author: student
"""
import requests
from bs4 import BeautifulSoup

res=requests.get("https://www.python.org/search/?q=dictionary&submit=")
if res.status_code==200:
    print("Success")
    print(res.content)
    
r_page=BeautifulSoup(res.content,"lxml")

first_ul=r_page.find('ul',{'class':"list-recent-events menu"})
list_a=first_ul.find_all('a')
print(len(list_a))
for a in list_a:
    #print(a.get_text())
    print(a['href'])

res1=requests.get("https://www.python.org/"+list_a)

#print(r_page.prettify())
#all_a_tags=r_page.find_all('a')
#print(type(all_a_tags))
#
#first_a=r_page.find('a')
#first_li=first_a.find('li')
#first_a1=first_li.find('a')
#print(first_a)
