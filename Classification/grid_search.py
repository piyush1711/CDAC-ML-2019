#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:56:18 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv(r"Social_Network_Ads.csv")
X=dataset.iloc[:,[2,3]].values
Y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

from sklearn.svm import SVC
classifier=SVC(kernel='rbf',random_state=0)
#classifier=SVC(kernel='poly',degree=7,random_state=0) ## by default degree=3
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)
 
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from sklearn.model_selection import cross_val_score
score1=cross_val_score(classifier,x_train,y_train,cv=10)
print(score1.mean())
#print(np.average(score1))
print(score1.std())



## Applying Grid Search to find the best model and the best parameters
from sklearn.model_selection import GridSearchCV
parameters = [{'C':[1,10,100,1000], 'kernel':['linear']},{'C':[1,10], 'kernel':['poly'],'degree':[2,3,4,5]},{'C':[1,10,100,1000], 'kernel':['rbf'],'gamma':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]}]
#parameters = [{'C':[1,10], 'kernel':['poly'],'degree':[2,3,4,5]}]
grid_search=GridSearchCV(estimator=classifier,param_grid=parameters,scoring='accuracy',cv=10,n_jobs=-1)
grid_search=grid_search.fit(x_train,y_train)
best_accuracy=grid_search.best_score_
best_parameters=grid_search.best_params_
## plot ROC Curve
