#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:31:45 2019

@author: student
"""

import numpy as np
a=np.array([1,2,3,4])
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
print(a)
b=np.array([(1,2,3),(4,5,6)])
c=np.array([[1,2],[3,4]],dtype=complex)
print(b)
print(c)
d=np.ones((2,3,4),dtype=np.int16)
print(d)
d=np.zeros((2,3),dtype=np.int16)
print(d)
d=np.empty((2,3),dtype=np.int16)
print(d)
d=np.arange(12)
print(d)
d=np.arange(12).reshape(4,3)
print(d)
d=np.arange(24).reshape(2,3,4)
print(d)
d=np.arange(12).reshape(2,6)
print(d)

a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
print(a)
print(b)
print(c)

print(a.dot(b))

b = b**2
print(b)

print(10*np.sin(b))
print(b)

a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])

c = a*b
print(c)

c = a.dot(b)
print(c)

c = np.dot(a,b)
print(c)


a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))

a *= 3
print(a)

b += a
print(b)

#a += b
#print(a)

a = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print(a)

a.resize((2,5))
print(a)


a = np.random.normal()
print(a)

a  = np.random.normal(size=4)
print(a)

a = np.random.uniform()
print(a)

a = np.random.uniform(size=4)
print(a)

a = np.random.randint(low=1, high=100, size=4)
print(a)


a = np.identity(3)
print(a)

a = np.identity(3, dtype=int)
print(a)

a = np.eye(3)
print(a)

a = np.eye(3,k=-1)
print(a)

a = np.eye(3, k=-2)
print(a)

a = np.eye(3, k=1)
print(a)


a = np.arange(28).reshape(7,4)
print(a)

for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*x
    
print(a)


