#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:47:51 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
age=pd.read_csv("age.csv")
x=age.iloc[:,1:8].values
y=age.iloc[:,8].values 


from sklearn.preprocessing import PolynomialFeatures
p_reg=PolynomialFeatures(degree=5)
x_poly=p_reg.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_poly,y,random_state=0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_poly,y)

y_pred=regressor.predict(x_test)

from sklearn.metrics import mean_squared_error,r2_score

mse = np.sqrt(mean_squared_error(y_test,y_pred))

r2score=r2_score(y_test,y_pred)

#plt.scatter(x,y,color='red')