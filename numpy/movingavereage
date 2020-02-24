#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:13:29 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as scp

datafile=pd.read_csv("/home/student/Desktop/old data/python/python/movavg.csv",index_col='Date')
#print(datafile)
#dataindex=pd.to_datetime(datafile.index)
#datafile.drop(columns='Unnamed: 0')
#print(datafile)
#
#weights=np.arange(1,11)
#sma10=datafile['Price'].rolling(10).mean()
#print("sma::",sma10.head(20))
#
#
#wma10=datafile['Price'].rolling(10).apply(lambda x:np.dot(x,weights)/sum(weights),raw='True')
#print("wma::",wma10.head(20))
#plt.figure(figsize=(12,6))
#plt.plot(datafile['Price'],label="price")
#plt.plot(wma10,label="10-Day WMA")
#plt.plot(sma10,label="10-Day SMA")
#plt.xlabel("Date")
#plt.xlabel("Price")
#
#ema10=datafile['Price'].ewm(span=10).mean()
#print(ema10.head(20))
#plt.plot(ema10,label="10-Day EMA")
#
#plt.legend()


datafile=pd.read_csv("/home/student/Desktop/python/dataset/MARUTI.NS.csv").head(20)
dataindex=pd.to_datetime(datafile.index)
print(datafile)

weights=np.arange(1,11)
sma10=datafile['High'].rolling(10).mean()
print("sma::",sma10.head(20))


wma10=datafile['High'].rolling(10).apply(lambda x:np.dot(x,weights)/sum(weights),raw='True')
print("wma::",wma10.head(20))
plt.figure(figsize=(12,6))
plt.plot(datafile['High'],label="high")
plt.plot(wma10,label="10-Day WMA")
plt.plot(sma10,label="10-Day SMA")
plt.xlabel("Date")
plt.xlabel("High")

ema10=datafile['High'].ewm(span=10).mean()
print(ema10.head(20))
plt.plot(ema10,label="10-Day EMA")

plt.legend()