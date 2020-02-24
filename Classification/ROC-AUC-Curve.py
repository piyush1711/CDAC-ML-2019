#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:52:12 2019

@author: student
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#roc_curve and auc score
from sklearn.datasets import make_classification
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


#plot ROC curve
def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color='orange',label='ROC')
    plt.plot([0,1],[0,1],color='darkblue',linestyle='--')
    plt.xlabel('Falss Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Charasteristic (ROC) Curve')
    plt.legend()
    
#generate data
data_X,class_label=make_classification(n_samples=1000,n_classes=2,weights=[1,1],random_state=1)

#step 4 split the data into train and test sub-dataset
trainX,testX,trainy,testy=train_test_split(data_X,class_label,test_size=0.3,random_state=1)

#step 5 fit a model on the train data
model=SVC(probability=True,random_state=0)
model.fit(trainX,trainy)

#step6 Predict probabilties for the test data
probs=model.predict_proba(testX)

#step7 keep probabilities of the positive class only
probs=probs[:,1]


#step8 compute the AUC Score.
auc=roc_auc_score(testy,probs)
print("AUC: %.2f" %auc)

#step9 get the ROC Curve
fpr,tpr,threshold=roc_curve(testy,probs)

#step10 : Plot ROC Curve using our defined function
plot_roc_curve(fpr,tpr)








