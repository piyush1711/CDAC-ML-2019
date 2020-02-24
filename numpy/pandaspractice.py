#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:38:08 2019

@author: student
"""

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])

print(s)
print(s[3:])
print(s.index) # will give index

d={'b':1,'a':0,'c':3}
print(d)
print(pd.Series(d)) #Dictionary ko Series Me conevert karta 
print(pd.Series(5.,index=['a','b','c','d','e'])) # will generate a series of value 5.0 as float data type
print(s.mean())
print(s[s>s.mean()])


print(s.median)
print(s[s>s.median()])


print(s[[4,3,1]]) # will give the values in particular position
print(s['b']) #Will give the value assigned to'b'
print('b' in s) # will give true false if presnt in dictionary or not
print(s.get('d')) # retrival using get function
print("--------------------")
print(s+s)
print(s*2)

