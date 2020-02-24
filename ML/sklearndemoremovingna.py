#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:12:09 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##Importing the dataset
#dataset=pd.read_csv('weather_data.csv')
#x=dataset.iloc[:,1:3].values
#
##y=dataset.iloc[:,3].values
#
##Taking care of missing data
from sklearn.preprocessing import Imputer
#
##create a object of Imputer class
impute =Imputer(missing_values='NaN',strategy='mean',axis=0)
impute=impute.fit(x[:,1:3])
x[:,1:3]=impute.transform(x[:,1:3])
print(x)
print(type(x))

df=pd.read_csv('housing.csv',na_values=[''])
#print(df['total_bedrooms'].head(566))
x=df.iloc[:,4].values
#print(x)
impute =Imputer(strategy='mean',axis=0)
x=x.reshape(-1,1)
impute=impute.fit(x[:])
print(impute.transform(x))