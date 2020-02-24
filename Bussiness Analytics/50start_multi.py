#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:51:46 2019

@author: student
"""

#Multiple Linear Regrssion

#Import the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the dataset
dataset=pd.read_csv("50_Startups.csv")
#print(type(dataset))
x=dataset.iloc[0:,:-1].values # values dataframe ko  ndarray me convert karta hai  
y=dataset.iloc[:,4].values # single coulumn so it will be in Series
#Printing the variables x & y
#print(x)
#print(y)
#Convert categorical data into numarical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#label Encoder
labelencoder=LabelEncoder()
x[:,3]=labelencoder.fit_transform(x[:,3])
#print(x)

#OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[3])
x=onehotencoder.fit_transform(x).toarray()
#print(x)
#Avioding the dummy varaible trap
x=x[:,1:]
print(x)

#Splitting the dataset into the Training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)



#fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression() # creating its object
regressor.fit(x_train,y_train)

# to Print Coefficent

print("Co-efficent:",regressor.coef_)
print("Intercepts:",regressor.intercept_)

y_pred=regressor.predict(x_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
print("mean squared:",np.sqrt(mean_squared_error(y_test,y_pred)))
print("mean absolute error:",mean_absolute_error(y_test,y_pred))








#To Get t_test value and p value

import statsmodels.api as sm

from scipy import stats
# this is backward elimination untill all  p values becomes less than 0.05
##adding Extra Collumn at the beginning
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
#x_opt=x[:,[0,1,2,3,4,5]]
#regressor_OLS=sm.OLS(endog=y,exog=x_opt)
#est=regressor_OLS.fit()
#print(est.summary())
# Remove variable 2 because p value is high
#x_opt=x[:,[0,1,3,4,5]]
#regressor_OLS=sm.OLS(endog=y,exog=x_opt)
#est=regressor_OLS.fit()
#print(est.summary())
# Remove variable 3 because p value is high
#x_opt=x[:,[0,3,4,5]]
#regressor_OLS=sm.OLS(endog=y,exog=x_opt)
#est=regressor_OLS.fit()
#print(est.summary())
# Remove variable 5 because p value is high
#x_opt=x[:,[0,3,4]]
#regressor_OLS=sm.OLS(endog=y,exog=x_opt)
#est=regressor_OLS.fit()
#print(est.summary())
# Remove variable 5 because p value is high
x_opt=x[:,[0,3]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt)
est=regressor_OLS.fit()
print(est.summary())

# this is backward elimination untill all  p values becomes less than 0.05
