#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:31:32 2019

@author: student
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('/home/student/Desktop/Data_Aug2019/Python/Programs/Clustering_demos/Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

#Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)   
plt.plot(range(1,11),wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.legend()
plt.show()
# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters=5,init='k-means++',random_state=42)
y_kmeans=kmeans.fit_predict(x)

# Visualising the Clusters
plt.scatter(x[y_kmeans == 0,0],x[y_kmeans ==0,1], s=100,c='red',label='Cluster 1')
plt.scatter(x[y_kmeans == 1,0],x[y_kmeans ==1,1], s=100,c='blue',label='Cluster 2')
plt.scatter(x[y_kmeans == 2,0],x[y_kmeans ==2,1], s=100,c='green',label='Cluster 3')
plt.scatter(x[y_kmeans == 3,0],x[y_kmeans ==3,1], s=100,c='orange',label='Cluster 4')
plt.scatter(x[y_kmeans == 4,0],x[y_kmeans ==4,1], s=100,c='cyan',label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow',label='Centroid')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
#plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')