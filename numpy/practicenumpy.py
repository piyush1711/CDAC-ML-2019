#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:31:56 2019

@author: student
"""
import numpy as np
a=np.array([1,7,3,4])
print(a)
print(a.ndim) # will return the array dimension
print(a.shape)
print(a.size)
print(a.dtype)# return Data tyoe of array
print(a.itemsize) # Item Size of int64
print(a.real)
print(a.nbytes)
print(a.data) # Memeory Location 
print(a.itemsize)
print(a.ctypes)
print(a.min())
print(a.max())
print(a.sum()) # Print Sum of all the 
print(a.mean())
print(a.fill(2)) # will fill all the values by 2
print(a)
print(a.flatten())
print(a.partition(2))
p=np.array([(1.5,55,3),(6,90,5)])
q=np.array([[1,4],[6,7]],dtype=complex)

print(q.dtype)
zero=np.zeros((3,4))
print(zero)

one=np.ones((2,3,4),dtype=np.int16)# 3d array
print(one)

r=np.arange(12) # will create range from 0 to 12
print(r)
o=np.arange(12).reshape(3,4) # will store range from 0 to 12 in 3 x 4 array
print(o)
f=np.arange(24).reshape(2,3,4)
print(f)
#################################33
l=np.array([20,30,40,50])
m=np.arange(4) # will generate a range 
su=l-m
print(su) # will give substraction element wise
print(l**2) # square of all th element in the list
print(10*np.sin(l))
print(l*m) # elementwise Product
##########################3333333
print(l)
print(m)
print(l.dot(m)) # matrix product
print(np.dot(l,m)) #another matrix Product


###################33333
k=np.ones((2,3),dtype=int)
j=np.random.random((2,3))
j+=k
print(j)
#k+=j    # float cannot be stored in integer
#print(k)

###########################33
r=np.arange(16).reshape(2,8)
print(r)
w=np.array([[2.,8.],[9.,6.],[4.,5.],[1.,1.],[8.,9.],[3.,6.]])
print(w)
w.resize((2,5))
print(w)

print(np.random.normal())

print(np.random.normal(size=4))
print(np.random.randint(low=1,high=100,size=4))


####################################################333
i=np.eye(3,3)
print(i)
i=np.eye(3,3,k=1) # will give idendity above the diagobal
print(i)
i=np.eye(3,3,k=-1) # will give idendity below the diagonal
i=np.eye(3,3,k=-1)
print(i)

###################

print(np.identity(4,dtype=int))

a=np.arange(28).reshape(7,4)
print(a)

for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x

print(a)

#############################3
a=np.arange(2,9).reshape(7,4)
print(a)
b=np.arange(3,15,4).reshape(3,1)
print(b)
for x,y in np.nditer([a,b]):
    print(x,y)








