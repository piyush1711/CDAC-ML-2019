#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:32:08 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
dataset_train=pd.read_excel("/home/student/Desktop/old data/python/python/Linear_regression.xlsx",skiprows=lambda x:x%3!=0)
dataset_test=pd.read_excel("/home/student/Desktop/old data/python/python/Linear_regression.xlsx",skiprows=lambda x:x%3==0)
x_train=dataset_test.iloc[:,0].values.reshape(-1,1)
y_train=dataset_test.iloc[:,1].values.reshape(-1,1)

x_test=dataset_train.iloc[:,0].values.reshape(-1,1)
y_test=dataset_train.iloc[:,1].values.reshape(-1,1)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print("Coefficrnt:M",regressor.coef_)
print("Intrceptor I ",regressor.intercept_)
y_pred=regressor.predict(x_test)
v=np.array([6.0]).reshape(1,-1)
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
#print(dataset.shape[0])
#x_train=[x for x in range(0,dataset.shape[0]) if x%3 == 0]
#y_train=[x for x in range(0,dataset.shape[0]) if x%2 == 0 ]
#xtrain=np.asarray(x_train).reshape(-1,1)
#print(xtrain)


























#x=dataset.iloc[:,:-1].values
#y=dataset.iloc[:,1].values