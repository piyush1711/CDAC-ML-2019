#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:17:09 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Social_Network_Ads.csv")
x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)



#Applying PCA
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#lda=LinearDiscriminantAnalysis(n_components=2)
#x_train=lda.fit_transform(x_train,y_train)
#x_test=lda.transform(x_test)
#explained_variance=lda.explained_variance_ratio_

from sklearn.decomposition import KernelPCA
kernelpca=KernelPCA(n_components=2,kernel='rbf')
x_train=kernelpca.fit_transform(x_train)
x_test=kernelpca.transform(x_test)



#from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
#qda=QuadraticDiscriminantAnalysis(priors=2)
#x_train=qda.fit(x_train,y_train)


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
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('blue','green')))


plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('blue','green'))(i),label=j)
    
plt.title('LDA Feature Extraction(training Set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()