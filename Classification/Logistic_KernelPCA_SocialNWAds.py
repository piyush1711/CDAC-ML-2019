#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:13:44 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv("/home/student/Desktop/Data_Aug2019/Python/Programs/Classification/Social_Network_Ads.csv")
X=dataset.iloc[:,2:4].values
Y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


### kernelPCA is useful only on non linear data
from sklearn.decomposition import KernelPCA
kpca=KernelPCA(n_components = 2, kernel='rbf')
x_train=kpca.fit_transform(x_train)
x_test=kpca.transform(x_test)
#explained_variance=pca.explained_variance_ratio_

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

### visualizing training set
from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
    
plt.title('Logistic Regression(Training Set)')
plt.xlabel('Kernal-PCA1')
plt.ylabel('Kernal-PCA2')
plt.legend()
plt.show()