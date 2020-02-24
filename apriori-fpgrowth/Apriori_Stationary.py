#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:11:17 2019
@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/student/Desktop/Data_Aug2019/Python/Programs/apriori-fpgrowth/off_stationary.csv', header = None)
df.columns = ['ID', 'Product']
g = df.groupby('ID')

transaction = []

for i in g:
    transaction.append(i[1]['Product'].values.tolist())
    

tr = {}
for i in transaction:
    for j in i:
        if tr.get(j, -1) != -1:
            tr[j].extend([k for k in i if k != j])
        else:
            tr[j] = []


reln = {}
for i, j in tr.items():
    for k in j:
        if reln.get((i, k), -1) != -1:
            reln[(i, k)] += 1
        else:
            reln[(i, k)] = 1
         
            
c = df.groupby('Product').count().reset_index()
final = {}
for i, j in reln.items():
    length = c[c['Product'] == i[0]]['ID'].values
    support = length/4386
    conf = j/length
    lift = conf/support
    final[i] = lift
    
final = pd.DataFrame.from_dict(final, orient='index').sort_values(0, ascending = False).reset_index()

recomendation = {}
cnt = 0
for i in final['index'].values:
    if recomendation.get(i[0], -1) != -1:
        recomendation[i[0]].append(i[1])
    else:
        recomendation[i[0]] = []
    cnt += 1
    if cnt > 10:
        break
    
for i, j in recomendation.items():
    print('Customer who buys', i, 'can also buy', end = ' ')
    for k in j:
        print(k, end = ', ')
    print()
        





    