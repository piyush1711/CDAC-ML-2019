#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:07:01 2019

@author: student
"""

import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('whitegrid')
#define the variable for the Percent to target based on historical results
avg=1
std_dev=.1
num_rep=500
num_simulation=1000
#Step 1: Generate random values for simulation model
# show how an exaple of calcuating the percent to target
pct_to_target=np.random.normal(avg,std_dev,num_rep).round(2)
#pct_to_target[0:10]

sales_target_values=[75_000,100_000,200_000,300_000,400_000,500_000]
sales_target_prob=[.3,0.3,0.2,.1,.05,.05]
sales_target=np.random.choice(sales_target_values,num_rep,p=sales_target_prob)
df=pd.DataFrame(index=range(num_rep),data={'Pct_to_Target':pct_to_target,'Sales_Target':sales_target})
df['sales']=df['Pct_to_Target']*df['Sales_Target']

def commissionrsate(x):
    if x>=0.90:
        return 0.03
    elif x==1.0:
        return 0.04
    elif x<=0.90:
        return 0.02
    
df['commissionrate']=df['Pct_to_Target'].apply(commissionrsate)
df.head(10)
df['commissionamt']=df['commissionrate']*df['sales']

budget=df['commissionamt'].sum()

