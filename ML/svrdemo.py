#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:28:55 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
age=pd.read_csv("age.csv")
x=age.iloc[:,1:8].values
y=age.iloc[:,8].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
#sc_x=StandardScaler()
sc_y=StandardScaler()

#x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

from sklearn.svm import SVR
regressor = SVR()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
#y_pred=sc_y.inverse_transform(y_pred)

from sklearn.metrics import mean_squared_error,r2_score

r2score=r2_score(y_test,y_pred)

#y_pred=regressor.predict(sc_x.fit_transform((np.array([6.5])).reshape(1,-1)))
