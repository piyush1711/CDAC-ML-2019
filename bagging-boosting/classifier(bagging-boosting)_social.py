#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:26:45 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier

dataset=pd.read_csv("/home/student/Desktop/Data_Aug2019/Python/Programs/bagging-boosting/Social_Network_Ads.csv")
X=dataset.iloc[:,[2,3]].values
Y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

classifier1=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier1.fit(x_train,y_train)
y_pred=classifier1.predict(x_test)
print("Decesion Tree Accuracy : ",accuracy_score(y_test,y_pred))

#step4 fit a andom forest model
classifier2=RandomForestClassifier(n_estimators=10, max_features="auto",criterion='entropy',random_state=0)
classifier2.fit(x_train,y_train)
y_pred=classifier2.predict(x_test)
print("Random Forest Accuracy : ",accuracy_score(y_test,y_pred))

#step5 fit a Adaboost model 
classifier3=AdaBoostClassifier(n_estimators=100)
classifier3.fit(x_train,y_train)
y_pred=classifier3.predict(x_test)
print("AdaBoost Classifier Accuracy : ",accuracy_score(y_test,y_pred))

#step6 fit a gradient boosting model
classifier4=GradientBoostingClassifier(n_estimators=100)
classifier4.fit(x_train,y_train)
y_pred=classifier4.predict(x_test)
print("GradientBoost Classifier Accuracy : ",accuracy_score(y_test,y_pred))


###first do pip install xgboost or conda install xgboost
from xgboost import XGBClassifier
classifier5=XGBClassifier()
classifier5.fit(x_train,y_train)

##predicting the test set results
y_pred=classifier5.predict(x_test)
print("XGBoostClassifier Accuracy : ",accuracy_score(y_test,y_pred))