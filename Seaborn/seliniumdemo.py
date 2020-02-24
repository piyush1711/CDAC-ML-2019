#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:24:56 2019

@author: student
"""
from selenium import webdriver
import time
# Create a new Firfox sessiom
driver=webdriver.Firefox(executable_path='/home/student/Desktop/geckodriver')
driver.implicitly_wait(30) # will wait til 30 milliseconds
driver.maximize_window()

#Navigate to th eapplication home page
driver.get('https://python.org')
# get the serach textbox
search_field=driver.find_element_by_name("q")
search_field.clear()

# enter search keyword amd submit
search_field.send_keys("list")
# taking name of go button and pressind it
search_submit=driver.find_element_by_name("submit")
search_submit.click()
# list me saare result lena Search all the result by class name
lists=driver.find_element_by_class_name("highlighted")
#print("Found"+str(len(lists))+"searches:")
print(str(lists.get_attribute("innerHTML")))

