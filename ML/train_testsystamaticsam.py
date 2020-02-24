#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:40:03 2019

@author: student
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
dataset=pd.read_csv("/home/student/Desktop/python/dataset/Salary_Data.csv")

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
#print(x)
#Splitiitng thd dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
print(x_train)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print("Coefficrnt:M",regressor.coef_)
print("Intrceptor I ",regressor.intercept_)

y_pred=regressor.predict(x_test)
v=np.array([10.0]).reshape(1,-1)
print(v.shape)

s=regressor.predict(v)
print(s)
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
print("Mean Squared:",np.sqrt(mean_squared_error(y_test,y_pred)))
print("Men Absolute Error:",mean_squared_error(y_test,y_pred))
print("R2 _score:",r2_score(y_test,y_pred))

#visualizarion
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')













# Ivsualizaation