#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:17:07 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
wine=pd.read_csv("/home/student/Desktop/Wine.csv")
x=wine.iloc[:,1:13].values
y=wine.iloc[:,13].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

#Applying PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)
explained_variance=pca.explained_variance_ratio_

#fitting Logistic Regression to the Training Model
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
    
# Predicting the test set results
y_pred=classifier.predict(x_test)

#confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)



from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max() +1,step=0.01),np.arange(start=x_set[:,1].min() -1,stop=x_set[:,1].max() +1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green','blue')))


plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green','blue'))(i),label=j)
    
plt.title('PCA Feature Extraction(training Set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()