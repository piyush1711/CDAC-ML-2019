#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:23:41 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/home/student/Desktop/Position_Salaries.csv")
print(data)
x=data.iloc[:,1].values
y=data.iloc[:,2].values
#print(x)
from sklearn.preprocessing import PolynomialFeatures

poly_reg=PolynomialFeatures(degree=3)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

from sklearn.linear_model import LinearRegression
lin_reg_2=LinearRegression()
lin_reg_2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='green')
plt.title("truth or Bluff (Polynomial Regreeeison)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(x),color='blue')
plt.title("truth or Bluff (Linear Regreeeison)") 
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
