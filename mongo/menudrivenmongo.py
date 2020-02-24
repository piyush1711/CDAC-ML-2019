#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:27:02 2019

@author: student
"""
import sys
import mongofunctions as m
from pymongo import MongoClient

client=MongoClient("localhost:27017")
print("connection done")

db=client.test

choice=0
while choice!=5:
    print("1. Insert")
    print("2. Update")
    print("3. Read")
    print("4. Delete")
    print("5. Exit")
    choice=int(input("Enter Choice :"))
    
    if choice==1:
        m.insert(db)
    elif choice==2:
        m.update(db)
    elif choice==3:
        m.read(db)
    elif choice==4:
        ans=m.delete(db)
        if ans:
            print("Deleted Successfully")
        else:
            print("Not Found")
    else:
        sys.exit(0)
    