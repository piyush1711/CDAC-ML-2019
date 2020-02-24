#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:03:51 2019

@author: student
"""

import numpy as np
import sys


mat1 = None
mat2 = None
mat3 = None

#def createMatrixByArange(r,c):
#    global mat1
#    mat1 = np.arange((r*c)).reshape(r,c)
#    print(mat1)

def createMatrixByArange(r,c):
    mat = np.arange((r*c)).reshape(r,c)
    return mat

#def createMatrixByRandom(r,c):
#    global mat2
#    mat2 = np.random.random((r,c))
#    print(mat2)

def createMatrixByRandom(r,c):
    mat = np.random.random((r,c))
    return mat


#def createMatrixByRandom2(r,c,x):
#    x = np.random.random((r,c))
#    print(x)

def createMatrixByRandom2(r,c):
    global mat3
    mat3 = np.random.random((r,c))
    print(mat3)

def displayShape(mat2):
    print("Matrix-1 Shape: ",mat1.shape)
    print("Matrix-2 Shape: ",mat2.shape)   

def matrixMupltiplication():
    print("Matrix Multiplication: ")
    print(mat1.dot(mat2))
    
def displayAll():
    print("Add: \n",mat1+mat3)
    print("Sub: \n",mat1-mat3)
    print("Mult: \n",mat1*mat3)


while True:
    print("1. Create Matrix by arrange")
    print("2. Create Matrix by random")
    print("3. Display Shape")
    print("4. Matrix Multiplication")
    print("5. Display Add, Sub, Mult")
    print("6. Exit")
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        row = int(input("Enter Rows: "))
        col = int(input("Enter Columns: "))
        mat1 = createMatrixByArange(row,col)
        print(mat1)
    elif choice == 2:
        row = int(input("Enter Rows: "))
        col = int(input("Enter Columns: "))
        mat2 = createMatrixByRandom(row,col) 
        print(mat2)
        #createMatrixByRandom2(row,col)
    elif choice == 3:
        displayShape(mat2)
    elif choice == 4:
        matrixMupltiplication()
    elif choice == 5:
        row = int(input("Enter Rows: "))
        col = int(input("Enter Columns: "))
        mat3 = createMatrixByRandom(row,col) 
        print(mat3)
        #createMatrixByRandom2(row,col)        
        displayAll()
    else:
        print("Exiting...")
        sys.exit(0)