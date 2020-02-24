#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:15:26 2019

@author: student
"""
import numpy as np
"""
a=np.arange(15).reshape(3,5)
print(a)
print("Shape:")
print(a.shape)
print("Size:")
print(a.size)
print("Type:")
print(type(a))
print("Creating An Array")
b=np.array([2,4,6])
print(b)
print("Data Type:",b.dtype)
print("Defining a new  2D array of ")
c=np.array([(1,5,15,12),(0,12,15,45)])
print("C",c)
print("Creating a array of consisting zeros")
z=np.zeros((3,4)) # Two brackts are complusary
print(z)
print("Creating a array of consisting Ones(1)")
o=np.ones((2,3)) # Two brackets are compulsary
print(o)
o1=np.ones((2,3),dtype=np.int16)
print(o1)

print("Basic Operations")
print("Element-wise")
a=np.array([20,30,40,50])
print(a)
b=np.array([10,20,22,17])
print(b)
c=a-b
print("Substraction Bit wise",c)
m=a*b
print("Multiplication",m)

print("Matrix Product 1",np.dot(a,b)) # same 
print("Matrrix Product 2:",a.dot(b)) # same

a=np.ones((2,3),dtype=int) # pehle row rehta hai bad be column nuber rehta hai 
print(a)
b=np.random.random((2,3))
print(b)
a*=3 # will multiply all elemets of a by 3

print(a)
print("********")
print(b)
b +=a # wil add all element of a to b and save it in b
print(b)

a=np.ones(3,dtype=np.int32)
b=np.linspace(0,pi,3)
print(b.dtype.name)
# Linspace generate a list from 4 to 10 having 5 elements
b=np.linspace(4,10,5)
print(b)

B = np.arange(3)
c=np.copy(B)
print(c)
"""
#import StringIO
#x = np.array([2,3,1,0])
#print(x)
x = np.array([2, 3, 1, 0])
print(x)
#x = np.array([[1,2.0],[0,0],(1+1j,3.)]) # note mix of tuple and lists,and types
#x = np.array([[ 1.+0.j, 2.+0.j], [ 0.+0.j, 0.+0.j], [ 1.+1.j, 3.+0.j]])

#data = "1, 2, 3\n4, 5, 6"
#np.genfromtxt(StringIO(data), delimiter=",")

print(x[2:-2])     
i=np.arange(10,1,-1)
print(i)
print(np.array([3,3,20,-8]),np.array([31,32,-8]))



