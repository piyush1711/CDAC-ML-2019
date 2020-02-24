#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:42:34 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Mall_Customers.csv")
x=dataset.iloc[:,[3,4]].values

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(x,method='ward',metric='euclidean'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc==0,0],x[y_hc==0,1],s=100,c='red',label='Cluster1')
plt.scatter(x[y_hc==1,0],x[y_hc==1,1],s=100,c='black',label='Cluster2')
plt.scatter(x[y_hc==2,0],x[y_hc==2,1],s=100,c='blue',label='Cluster3')
plt.scatter(x[y_hc==3,0],x[y_hc==3,1],s=100,c='green',label='Cluster4')
plt.scatter(x[y_hc==4,0],x[y_hc==4,1],s=100,c='pink',label='Cluster5')
#plt.scatter(hc.cluster_centers_[:,0],hc.cluster_centers_[:,1],s=50,c='yellow',label='Centroid')
plt.title('Clusters Method')
plt.show()