#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:58:07 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/student/Desktop/old data/python/python/dataset/aapl.csv"
df=pd.read_csv(path)
low=df['Low']
print("Min:",low.min())
print("Max:",low.max())
print("Max -Min:",low.max()-low.min())
print("VaraincE:",low.var())
print("SD:",low.std())
quartile=df['Low'].quantile(0.75)
print(quartile)
quartile1=df['Low'].quantile(0.25)
print("Q1:",quartile1)
itr=quartile-quartile1
print("IQR:",itr)
plt.boxplot(low,itr)