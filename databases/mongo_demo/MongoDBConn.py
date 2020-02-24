#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:08:26 2019

@author: student
"""
from pymongo import MongoClient

client=MongoClient('localhost:27017')
print("Connection Established")

db=client.EmployeeData
Eid=input("Enter Employee id: ")
Ename=input("Enter Name ")
Eage=input("Enter Age ")
Ecountry=input("Enter Country : ")

db.Employees.insert_one(
        {
            "eid":Eid,
            "name":Ename,
            "age":Eage,
            "Country":Ecountry
        })