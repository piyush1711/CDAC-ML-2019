#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:43:34 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

multi=pd.read_excel("Multple Regression Analyisis_1.xlsx")
print(type(multi))
x=multi.iloc[:,:-1].values
y=multi.iloc[:,5].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print("Coffient:",regressor.coef_)
print("Interceptor:",regressor.intercept_)

y_pred=regressor.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
print("mean squared:",np.sqrt(mean_squared_error(y_test,y_pred)))
print("mean absolute error:",mean_absolute_error(y_test,y_pred))
 
import statsmodels.api as sm
from scipy import stats
#x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
x_opt=x[:,[0,1,2,3,4]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt)
est=regressor_OLS.fit()
print(est.summary())