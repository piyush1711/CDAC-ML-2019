#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:34:10 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Data Preprocessing 
dataset=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
transactions=[]
for i in range(7501):
    transactions.append([str(dataset.values[i,j])for j in range(0,20)])
    #training Apriori on the dataset

from apyori import apriori
rules=apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_lenght=2)
#Visualiing the results
results=list(rules)
u=0
for j in range(0,10):
    print(results[u].items)
    u=u+1
