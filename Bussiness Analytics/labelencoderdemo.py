#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:53:16 2019

@author: student
"""


import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
dataset=pd.read_excel("stock_data.xlsx",na_values=['n.a.','not available',-1])

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
print(y)

 

#print(x)

onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
#print(pd.DataFrame(x))
 
 
labelencoder_Y=LabelEncoder()
y=labelencoder_Y.fit_transform(y[:,4])
#print(x)
#
#onehotencoder=OneHotEncoder(categorical_features=[0])
#x=onehotencoder.fit_transform(x).toarray()
#print(pd.DataFrame(x))
# 
