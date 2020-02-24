#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:41:33 2019

@author: student
"""

from scipy.stats import uniform,norm,gamma,expon,poisson,binom
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

n=10000
start=10
width=20


data_uniform=uniform.rvs(size=n,loc=start,scale=width)
ax=sns.distplot(data_uniform,bins=100,kde=False,color='skyblue',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Uniform Distribution',ylabel='Frequency')


data_normal=norm.rvs(size=n,loc=start,scale=width)
ax=sns.distplot(data_normal,bins=100,kde=False,color='green',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Normal Distribution',ylabel='Frequency')


data_gamma=gamma.rvs(a=5,size=10000)
ax=sns.distplot(data_gamma,bins=100,kde=False,color='green',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Gamma Distribution',ylabel='Frequency')


data_expon=expon.rvs(scale=1,loc=0,size=10000)
ax=sns.distplot(data_expon,bins=100,kde=False,color='green',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Exponential Distribution',ylabel='Frequency')


data_poisson=poisson.rvs(mu=3,size=10000)
ax=sns.distplot(data_poisson,bins=30,kde=False,color='green',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Poisson Distribution',ylabel='Frequency')

data_binom=binom.rvs(n=10,p=0.8,size=10000)
ax=sns.distplot(data_binom,bins=30,kde=False,color='green',hist_kws={"linewidth":15,'alpha':1})
ax.set(xlabel='Binomial Distribution',ylabel='Frequency')

#prob mass function

num_throws = 10000
outcomes = np.zeros(num_throws)
for i in range(num_throws):
    outcome = np.random.choice(['1','2','3','4','5','6'])
    outcomes[i] = outcome
    
val, cnt = np.unique(outcomes, return_counts=True)

prop = cnt/len(outcomes)
plt.bar(val, prop)
plt.ylabel('prob')
plt.xlabel('outcome')
plt.show()
plt.close()