#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:27:38 2019

@author: student
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient

def insert():
    try:
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
        print("\n Inserted data succesfully\n")
    except Exception as e:
        print(str(e))
        


client=MongoClient('localhost:27017')
print("Connection Established")



def read():
    try:
        empcol=db.Employees.find()
        for emp in empcol:
            print(emp)
    except Exception as e:
        print(str(e))


def update():
    try:
        criteria=input("Enter id to update : ")
        name=input("Enter name to update")
        age=input("Enter age to update")
        country=input("Enter country to update")
        
        db.Employees.update_one({"eid":criteria},
                                {
                                "$set":{
                                        "name":name,
                                        "age":age,
                                        "Country":country
                                        }
                                })
        print("Updated Successfully")
    except Exception as e:
        print(str(e))
        
        
def delete():
    try:
        criteria = input("Enter Id to delete")
        db.Employees.delete_many({"eid": criteria})
        print("Deleted successfully")
    except Exception as e:
        print(str(e))


db=client.EmployeeData
selection="0"
while selection!="5":
    selection=input("\nselect \n1.insert, \n2.update,\n3.read,\n4.delete \n5.Exit")
    
    if selection=="1":
        insert()
    elif selection=="2":
        update()
    elif selection=="3":
        read()
    elif selection=="4":
        delete()
    elif selection=="5":
        sys.exit(0)
    else:
        print("Invalid Selection\n")
        


