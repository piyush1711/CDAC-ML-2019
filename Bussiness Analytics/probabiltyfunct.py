#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:44:13 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as scp
#uniform Distribution
#data_uniform=scp.uniform.rvs(size=1000,loc=24,scale=20)
#ax=sns.distplot(data_uniform,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":12,'alpha':1})
ax.set(xlabel='UniformDistribution',ylabel='Freqency')
#Normal Distribution
#data_uniform=scp.norm.rvs(size=1000,loc=24,scale=20)
#ax=sns.distplot(data_uniform,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":15,'alpha':1})
#Gamma Distribution
#data_uniform=scp.gamma.rvs(a=5,size=1000,loc=24,scale=20)
#ax=sns.distplot(data_uniform,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":15,'alpha':1})

#Exponential Curve
#data_uniform=scp.expon.rvs(scale=1,loc=0,size=1000)
#ax=sns.distplot(data_uniform,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":15,'alpha':1})
## Poission Distribution
#data_uniform=scp.poisson.rvs(mu=3,size=100000)
#print(len(data_uniform))
#ax=sns.distplot(data_uniform,bins=30,kde=False,color='skyblue',hist_kws={"linewidth":15,'alpha':1})
data_binom=scp.binom.rvs(n=10,p=0.8,size=10000)
ax=sns.distplot(data_binom,bins=100,kde=True,color='skyblue',hist_kws={"linewidth":15,'alpha':1})