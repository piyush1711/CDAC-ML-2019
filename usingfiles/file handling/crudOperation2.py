# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from pymongo import MongoClient

def insert():
    try:
        pid = input('Enter Product id : ')
        pname = input('Enter Product name : ')
        quantity = input('Enter Product Quantity : ')
        price =input('Enter Product Price :')
        db.product.insert_one(
        {
        "pid": pid,
        "name": pname,
        "quantity": quantity,
        "price": price
        }
        )
        print("Data inserted successfully")
    except Exception as e:
        print(str(e))
def read():
    st2=db.product.find()
    for j in st2:
        print(j)

def update():
     try:
         criteria=input("Enter pid to update : ")
         pname = input("Enter name to update : ")
         quantity = input("Enter quantity : ")
         price=input("Enter price : ")
         db.product.update_one(
                 {"pid":criteria},
                 {
                 "$set":{
                         "name":pname,
                         "quantity":quantity,
                         "price":price
                         }})
         print("Updated sucessfully")
     except Exception as e:
         print(str(e))
def delete():
     try:
         criteria= input("Enter the product id to delete :")
         db.product.delete_many({"pid":criteria})
         print("Deleted successfully")
     except Exception as e:
         print(str(e))


client = MongoClient('localhost:27017')
print("Connection Done")

db=client.test
selection=0

while selection!=5:
    selection = input('1. Insert\n2. Update\n3. Read\n4. Delete\n5. Exit\nSelect an option : ')
    if selection == '1':
        insert()
    elif selection == '2':
        update()
    elif selection == '3':
        read()
    elif selection == '4':
        delete()
    else:
        sys.exit(0)
