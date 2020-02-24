#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:19:48 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#load Library
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier


# Step1 Create dataset
# noise is standard deviationof gaussian noise added to the data
# by default noise is none it can be any double number
X, Y = make_moons(n_samples=10000, noise=0.5, random_state=0)


#Step2: splitting in train and test set
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


### fit a logistic regressor model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("Logistic Regressor Accuracy : ",accuracy_score(y_test,y_pred))


#step3 fit a decesion tree model as comparison
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



























