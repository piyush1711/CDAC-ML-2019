#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:44:55 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

age_data=pd.read_csv("age.csv")
x=age_data.iloc[:,1:8].values
y=age_data.iloc[:,8].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

print("co-efficient:",regressor.coef_)
#print("intercept:",regressor.)
print("Interceptor:",regressor.intercept_)
print("mean squared:",np.sqrt(mean_squared_error(y_test,y_pred)))
print("mean absolute error:",mean_absolute_error(y_test,y_pred))
import statsmodels.api as sm
from scipy import stats
#x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
x_opt=x[:,[0,1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt)
est=regressor_OLS.fit()
print(est.summary())