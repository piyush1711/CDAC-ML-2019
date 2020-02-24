#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:25:44 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path="/home/student/Desktop/old data/python/python/dataset/aapl.csv"
df=pd.read_csv(path)
low=df['Low']
mean=low.mean()
print(mean)
mode=low.mode()
print(mode[5])
median=low.median()
print(median)
plt.figure(figsize=(10,5))
plt.hist(low,bins=100,color='grey')
plt.axvline(mean,color='red',label='mean')
plt.axvline(median,color='green',label='median')
plt.axvline(mode[3],color='yellow',label='mode')
plt.legend()
