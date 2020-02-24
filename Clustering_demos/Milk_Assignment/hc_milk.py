#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:23:26 2019

@author: student
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('milk.csv')
x=dataset.iloc[:,1:6]

from sklearn.decomposition import PCA
pca=PCA(n_components = 2)
x=pca.fit_transform(x)
explained_variance=pca.explained_variance_ratio_

## Using dendrogram to find the optimal no of clusters
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('milk')
plt.ylabel('Euclidean Distance')
plt.show()

## Fitting Hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering 
hc=AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

# Visualising the Clusters
plt.scatter(x[y_hc == 0,0],x[y_hc ==0,1], s=100,c='red',label='Cluster 1')
plt.scatter(x[y_hc == 1,0],x[y_hc ==1,1], s=100,c='blue',label='Cluster 2')
plt.scatter(x[y_hc == 2,0],x[y_hc ==2,1], s=100,c='green',label='Cluster 3')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()