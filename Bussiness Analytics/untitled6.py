#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:20:12 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
dataset1=pd.read_csv("/home/student/Desktop/python/dataset/Salary_Data.csv",skiprows=lambda i:(i%2!=0))
dataset2=pd.read_csv("/home/student/Desktop/python/dataset/Salary_Data.csv",skiprows=lambda i:(i%2==0))
x=dataset1.iloc[:,1]
y=dataset1.iloc[:,1]
x_mean=x.mean(x)
y_mean=y.mean()


from scipy.stats import ttest_ind
ttest,pval=ttest_ind(x,y)
print("P-Value:",pval)