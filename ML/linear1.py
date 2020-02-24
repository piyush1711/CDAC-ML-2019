#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:30:07 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/home/student/Desktop/Position_Salaries.csv")
print(data)
x=data.iloc[:,1].values.reshape(-1,1)
y=data.iloc[:,2].values.reshape(-1,1)
#print(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
#print(x_train)
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(x_train,y_train)

print("Coffient:",regressor.coef_)
print("Interceptor:",regressor.intercept_)

y_pred=regressor.predict(x_test)
plt.scatter(x_train,y_train)
plt.plot(x_train,regressor.predict(x_train))
plt.show()
print(regressor.predict(x_train))
plt.scatter(x_train,y_train)
plt.plot(x_test,regressor.predict(x_test))
plt.show()