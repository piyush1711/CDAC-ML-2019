#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:37:36 2019

@author: student
"""

import numpy as np
import pandas as pd

s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print(s)


print(s[:3])



d={'b':1,'c':0,'d':2}
e=pd.Series(d)

print(e)




c=pd.Series(2.,index=['a','b','c','d','e'])
print(c)


print(s[s>s.median()])
print(s[[2,3]])


if 'ee' in s:
    print("yes")
else:
    print("no")
    
    
#print(s['f'])
#print(s['e'])


print(s+s)











