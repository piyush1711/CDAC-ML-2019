#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:24:48 2019

@author: student
"""


#import sys
#sys.path.append(r"/home/student/Desktop/Data_Aug2019/")
#### not needed


#from selenium import webdriver
#
#driver = webdriver.Firefox(executable_path='/home/student/Desktop/Data_Aug2019/geckodriver')
#driver.get('https://python.org')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create new firefox session
driver = webdriver.Firefox(executable_path='/home/student/Desktop/Data_Aug2019/geckodriver')
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to application homepage
driver.get('https://python.org')

#get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

#enter search keyword and submit
search_field.send_keys("Dictionary")
go_field = driver.find_element_by_id("submit")
go_field.click()
driver.implicitly_wait(40)
#get the list of elements whwich are displayed

#print("Hi...")
lists = driver.find_elements_by_class_name("list-recent-events") 
print("found "+str(len(lists))+" searches.")

#print("Hi")
#for l in lists:
#    print(l.find_element_by_tag_name("a").get_attribute("innerHTML"))

for l in lists:
    ls = l.find_elements_by_tag_name("a")
    for i in ls:
        print(i.get_attribute("innerHTML"))

driver.quit()