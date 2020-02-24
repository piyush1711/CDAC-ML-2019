#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:16:25 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
housing=pd.read_csv("Housing.csv")
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



from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=10)
x_poly=poly_reg.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_poly,y,random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_poly,y)
y_pred=regressor.predict(x_test)