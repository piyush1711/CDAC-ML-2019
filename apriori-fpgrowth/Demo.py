#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:15:36 2019

@author: student
"""

import pandas as pd 

#Data Preprocessing
dataset=pd.read_csv(r"/home/student/Desktop/Data_Aug2019/Python/Programs/apriori/Market_Basket_Optimisation.csv", header=None)
transactions=[]

for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Training Apriori in the dataset   
from apyori import apriori
rules = apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)

# visualizing the results
results=list(rules)

i=0
for i in range(1,10):
    print(results[i].items)
#print(results[1].items)