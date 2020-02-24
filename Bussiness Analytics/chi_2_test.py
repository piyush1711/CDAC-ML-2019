#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:54:20 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

a1=[6,4,5,10]
a2=[8,5,3,3]
a3=[6,4,5,3]
a4=[6,4,3,2]
a5=[6,4,6,3]
a6=[6,4,5,1]
a7=[6,4,5,5]
dice=np.array([a1,a2,a3,a4,a5,a6,a7])
from scipy import stats

chi2_stat,pval,dof,e=stats.chi2_contingency(dice)
print("===Chi2 Stat++")
print(chi2_stat)
print("DOf:",dof)
print("P-value",pval)
