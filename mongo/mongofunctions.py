#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:31:27 2019

@author: student
"""

def insert(db):
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
    
def read(db):
    ans=db.employee.find()
    for i in ans:
        print(i)
        
def delete(db):
    eid=input("Enter Id to be deleted : ")
    ans=db.employee.find_one({'id':eid})
    print(ans)
    aa=input("Confirm Deletion(y/n)")
    if aa=="y":
        db.employee.delete_one({'id':eid})
        return True
    else:
        return False

def update(db):
    eid=input("Enter the Id to be Updated:")
    name=input("Enter the name to be updated:")
    country=input("Enter the Country name to be changes")
    age=input("Enterthe age:")
    db.employee.update_one(
            {"id":eid},
             {
            "$set":{
                     "name":name,
                     "age":age,
                     "country":country
                }})
    print("Record Upated Successfully")
    