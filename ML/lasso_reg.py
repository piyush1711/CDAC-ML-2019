#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:29:50 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

boston=load_boston()
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)

boston_df['Price']=boston.target

newX=boston_df.drop('Price',axis=1)
print(newX[0:3])
newY=boston_df['Price']
x_train,x_test,y_train,y_test=train_test_split(newX,newY,test_size=0.3)
print(len(x_test),len(y_test))
lr=LinearRegression()
lr.fit(x_train,y_train)
#Ridge Regresison
rd=Lasso(alpha=0.01)
rd.fit(x_train,y_train)
rd100=Lasso(alpha=50)
rd100.fit(x_train,y_train)
train_score=lr.score(x_train,y_train)
test_score=lr.score(x_test,y_test)
Ridge_train_score=rd.score(x_train,y_train)
Ridge_test_score=rd.score(x_test,y_test)
Ridge_train_score100=rd100.score(x_train,y_train)
Ridge_test_score100=rd100.score(x_test,y_test)

print(rd)
print(rd100)
print("Coeff",lr.coef_)
print(Ridge_train_score)
print(Ridge_test_score)
print(Ridge_train_score100)
print(Ridge_test_score100)