#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:17:55 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#mean, median,mode
path = "weather_by_cities.csv"
df = pd.read_csv(path)

ws = df['windspeed']

print(ws)
mean_ws = ws.mean()
median_ws = ws.median()
mode_ws = ws.mode()
print(type(mode_ws))

print("mean: ", mean_ws, "median: ", median_ws,"mode: ",mode_ws.values)
plt.figure(figsize=(10,5))
plt.hist(ws,bins=10,color='grey')
plt.axvline(mean_ws,color='red',label='Mean')    
plt.axvline(median_ws,color='blue',label='Median')
plt.axvline(mode_ws[0],color='green',label='Mode')
plt.xlabel('Windspeed')
plt.ylabel('Frequency')
plt.legend()
plt.show()