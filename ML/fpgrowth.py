#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:27:20 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyfpgrowth
dataset=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
transactions=[]
for i in range(0,7501):
    lst=[]
#    transactions.append([str(dataset.values[i,j])for j in range(0,20)])
    
    for j in range(0,20):
        if str(dataset.values[i,j])!='nan':
            lst.append(str(dataset.values[i,j]))
        transactions.append(lst)
patterns = pyfpgrowth.find_frequent_patterns(transactions,2)
rules=pyfpgrowth.generate_association_rules(patterns,0.2)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix()
