#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:58:01 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

#mean, median,mode
path = "weather_by_cities.csv"
df = pd.read_csv(path)

ws = df['windspeed']

print("Min :",ws.min())
print("Max :",ws.max())
print('range:',ws.max()-ws.min())
print("var :",round(ws.var(),2))
print("SD :",round(ws.std(),2))
print("SD :",round(sqrt(ws.var()),2))
print("50th percentile :",ws.quantile(0.5))
print("75th percentile :",ws.quantile(0.75))
print("25th percentile :",ws.quantile(0.25))
print('IQR: ', ws.quantile(0.75)-ws.quantile(0.25))



plt.boxplot(ws)
plt.show()