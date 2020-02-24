#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 08:56:46 2019

@author: student
"""

from pymongo import MongoClient
client=MongoClient("localhost:27017")
print("connection done")

db=client.test
eid=input("Enter Employee Id :")
ename=input("Enter name :")
eage=input("Enter Age :")
country=input("Enter Country :")

db.employee.insert_one(
        {
                "id":eid,
                "name":ename,
                "age":eage,
                "country":country           
        })