#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:16:35 2019

@author: student
"""

import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')
import matplotlib.pyplot as plt
df=pd.read_csv("Position_Salaries.csv")
x=df.iloc[:,1:2].values
y=df.iloc[:,2:3].values

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)

from sklearn.svm import SVR
regressor=SVR()
regressor.fit(x,y)


y_pred=regressor.predict(sc_x.fit_transform((np.array([6.5])).reshape(1,-1)))
y_pred=sc_y.inverse_transform(y_pred)
from sklearn.model_selection import cross_val_score
scores=cross_val_score(regressor,x,y)
print(scores)
print(np.average(scores))

plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title('Truth or Bluff(SCR)')
plt.xlabel("Position Level")
plt.ylabel('Salary')
plt.show()

x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid),color='blue')
plt.title('Truth or Bluff(SCR)')
plt.xlabel("Position Level")
plt.ylabel('Salary')
plt.show()
