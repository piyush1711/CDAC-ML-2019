#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:46:14 2019

@author: student
"""
import numpy as np
import matplotlib.pyplot as plt
numthrows=1000
outcomes=np.zeros(numthrows)
for j in range(numthrows):
    outcome=np.random.choice(['1','2','3','4','5','6'])
    outcomes[j] = outcome
val,count = np.unique(outcomes,return_counts=True)
prop=count/len(outcomes)
plt.bar(val,prop)
plt.xlabel("Probabity")
plt.ylabel("Outcome")
plt.show()
plt.close()