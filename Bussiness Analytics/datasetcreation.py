#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:11:21 2019

@author: student
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

a=np.random.random(1000)
print(a)
ages=np.random.normal(20,40,size=1000)
age_mean=np.mean(ages)
print("Mean:",age_mean)
tset,pval=ttest_1samp(ages,30)
print("P-Value:",pval)
if pval<0.05:
    print("Null Hypothesis Rejected")
else:
    print("Accepted")







#print(b)
#import seaborn as sns
#sns.distplot(b,bins=20)
