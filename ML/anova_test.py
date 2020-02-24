#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:14:38 2019

@author: student
"""
#Load ackages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Load the file
d=pd.read_csv("a.txt", sep="\t")
#generate a boxplot to see the data distribution by treatment betwn different treatments
d.boxplot(column=['A','B','C','D'],grid=False)

#Load Packages
import scipy.stats as stats
#stats f_oneway(0 takes the group as input and return 
fvalue,pvalue=stats.f_oneway(d['A'],d['B'],d['C'],d['D'])
print(fvalue,pvalue)
from statsmodels.formula.api import ols
d_melt=pd.melt(d.reset_index(),id_vars=['index'],value_vars=['A','B','C','D'])
d_melt.columns=['index','performance','value']
model=ols('value~C(performance)',data=d_melt).fit()
anova_table=sm.stats.anova_lm(model,typ=2)
print(anova_table)

from statsmodels.stats.multicomp import pairwise_turkeyhsd
m_comp_res = pairwise_turkeyhsd(endog=d_melt['value'],groups=d_melt['performance'],alpha=0.05)

print(m_comp_res)