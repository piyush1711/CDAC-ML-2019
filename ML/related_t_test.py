#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:22:04 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


ds1=np.random.normal(2.3,0.9,1000)
ds2=np.random.normal(1.8,0.7,1000)
ds1_mean=np.mean(ds1)
ds2_mean=np.mean(ds2)
print("Mean:\t%d\t %d"%(ds1_mean,ds2_mean))
ds1_std=np.std(ds1)
ds2_std=np.std(ds2)
ttest,pval=stats.ttest_rel(ds1,ds2)
print("P-value:",pval)
if pval<0.05:
    print("We are Reject Null hypothesis")
else:
    print("Acceptes")