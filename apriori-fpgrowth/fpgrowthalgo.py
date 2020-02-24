#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:24:22 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

import pyfpgrowth


dataset=pd.read_csv(r"/home/student/Desktop/Data_Aug2019/Python/Programs/apriori-fpgrowth/Market_Basket_Optimisation.csv", header=None)


transactions=[]

for i in range(0,7501):
#    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    lst=[]
    for j in range(0,20):
        if str(dataset.values[i,j])!="nan":
            lst.append(str(dataset.values[i,j]))
    transactions.append(lst)
    
print("Generating Pattern")
pattern=pyfpgrowth.find_frequent_patterns(transactions,2)

print("Generating Rules")
rules=pyfpgrowth.generate_association_rules(pattern,0.2)