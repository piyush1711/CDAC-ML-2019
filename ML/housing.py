#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:13:46 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
housing=pd.read_csv("Housing.csv")

#print(x)
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
housing['driveway']=labelencoder.fit_transform(housing['driveway'])
housing['recroom']=labelencoder.fit_transform(housing['recroom'])
housing['fullbase']=labelencoder.fit_transform(housing['fullbase'])
housing['gashw']=labelencoder.fit_transform(housing['gashw'])
housing['airco']=labelencoder.fit_transform(housing['airco'])
housing['prefarea']=labelencoder.fit_transform(housing['prefarea'])



x=housing.iloc[:,1:].values
y=housing.iloc[:,0].values


print(housing)



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
x_opt=x[:,[0,1,2,3,4,5,6,7,8,9,10]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt)
est=regressor_OLS.fit()
print(est.summary())




