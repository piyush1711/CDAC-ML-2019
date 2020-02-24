#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:53:24 2019

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
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)

y_pred=regressor.predict(np.array(6.5).reshape(1,-1))
print(y_pred)
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