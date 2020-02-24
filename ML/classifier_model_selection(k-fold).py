#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:26:45 2019

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


#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
y_pred1=classifier.predict(x_test)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train_svc=sc.fit_transform(x_train)
x_test_svc=sc.transform(x_test)

#SVC
from sklearn.svm import SVC
svcclassifier = SVC(kernel='linear',random_state=0)
svcclassifier.fit(x_train_svc,y_train)
y_pred2=svcclassifier.predict(x_test_svc)

from sklearn.svm import SVC
svcclassifier1 = SVC(kernel='poly',random_state=0)
svcclassifier1.fit(x_train_svc,y_train)
y_pred21=svcclassifier1.predict(x_test_svc)

from sklearn.svm import SVC
svcclassifier2 = SVC(kernel='rbf',random_state=0)
svcclassifier2.fit(x_train_svc,y_train)
y_pred22=svcclassifier2.predict(x_test_svc)

from sklearn.ensemble import RandomForestClassifier
random_classifier=RandomForestClassifier(n_estimators=10,criterion="entropy",random_state=0)
random_classifier.fit(x_train,y_train)

y_pred=random_classifier.predict(x_test)

from sklearn.tree import DecisionTreeClassifier
decision_classifier=DecisionTreeClassifier(criterion="entropy",random_state=1)
decision_classifier.fit(x_train,y_train)

y_pred=decision_classifier.predict(x_test)


#Predicting the Test set Result
#1--------------
from sklearn.model_selection import cross_val_score

accuracy = cross_val_score(classifier,x_train,y_train,cv=5)
#accuracy = cross_val_score(classifier,x,y,cv=5)
#print("LOgostic::",accuracy.mean()*100)
#------------------------
accuracysvc=cross_val_score(svcclassifier,x,y,cv=5)
##print("SVC::linear:",accuracysvc.mean()*100)
#
accuracysvc1=cross_val_score(svcclassifier1,x,y,cv=5)
##print("SVC::Poly:",accuracysvc1.mean()*100)
#
accuracysvc2=cross_val_score(svcclassifier2,x,y,cv=5)
##print("SVC:RBF:",accuracysvc2.mean()*100)
#
random_forest_accuracy=cross_val_score(random_classifier,x,y,cv=5)
##print("Random-Classfier",random_forest_accuracy.mean()*100)
#
decision_accuracy=cross_val_score(decision_classifier,x,y,cv=5)
##print("Decision-Classfier",decision_accuracy.mean()*100)

#
#
lst=[accuracy.mean()*100,accuracysvc.mean()*100,accuracysvc1.mean()*100,random_forest_accuracy.mean()*100,decision_accuracy.mean()*100]
print("Max Accuracy Mean in All model is:",lst.max())

