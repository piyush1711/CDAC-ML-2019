#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:01:02 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
dataset=read_csv("/home/student/Desktop/python/dataset/Salary_Data.csv")

ds1=np.random.normal(2.3,0.9,1000)
ds2=np.random.normal(1.8,0.7,1000)
ds1_mean=np.mean(ds1)
ds2_mean=np.mean(ds2)
ds1_std=np.std(ds1)
ds2_std=np.std(ds2)
ttest,pval=ttest_ind(ds1,ds2)
print("P-value:",pval)
if pval<0.05:
    print("We are Reject Null hypothesis")
else:
    print("Acceptes")
