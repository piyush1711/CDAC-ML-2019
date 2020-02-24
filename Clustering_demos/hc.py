#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:45:39 2019

@author: student
"""

import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv('/home/student/Desktop/Data_Aug2019/Python/Programs/Clustering_demos/Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

## Using dendrogram to find the optimal no of clusters
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()


## Fitting Hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering 
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

# Visualising the Clusters
plt.scatter(x[y_hc == 0,0],x[y_hc ==0,1], s=100,c='red',label='Cluster 1')
plt.scatter(x[y_hc == 1,0],x[y_hc ==1,1], s=100,c='blue',label='Cluster 2')
plt.scatter(x[y_hc == 2,0],x[y_hc ==2,1], s=100,c='green',label='Cluster 3')
plt.scatter(x[y_hc == 3,0],x[y_hc ==3,1], s=100,c='orange',label='Cluster 4')
plt.scatter(x[y_hc == 4,0],x[y_hc ==4,1], s=100,c='cyan',label='Cluster 5')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
