#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:18:21 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
age=pd.read_csv("age.csv")
x=age.iloc[:,1:8].values
y=age.iloc[:,8].values 


from sklearn.preprocessing import PolynomialFeatures
p_reg=PolynomialFeatures(degree=7)
x_poly=p_reg.fit_transform(x)
#p_reg.fit(x_poly,y)


from sklearn.linear_model  import LinearRegression
l_reg=LinearRegression()
l_reg.fit(x_poly,y)

plt.scatter(x_poly,y,color='red')
plt.plot(x,l_reg.predict(p_reg.fit_transform(x)),color='green')