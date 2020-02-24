#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:51:48 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color='orange',label='ROC')
    plt.plot([0,1],[0,1],color='darkblue',linestyle='--')
    plt.xlabel('FalsePositiveRate')
    plt.ylabel('TruePositiveRate')
    plt.title("Reciver Operaring Characterstics(ROC) Curve")
    plt.legend()
    
    #generate Data
data_x,class_label=make_classification(n_samples=1000,n_classes=2,weights=[1,1],random_state=1)

#Step4:Split the data into train & test
trainx,testx,trainy,testy=train_test_split(data_x,class_label,test_size=0.3,random_state=1)
#Step5:Fit a model on the train data
model=SVC(probability=True,random_state=0)

model.fit(trainx,trainy)
#step6: Predict probability for the test data.
probs=model.predict_proba(testx)
#step7: Keep  Probability of positye class onlt
probs=probs[:,1]
#step*: compute the AUc Score
auc=roc_auc_score(testy,probs)
print('AUC:%.2f'% auc)


fpr,tpr,tresholds=roc_curve(testy,probs)
plot_roc_curve(fpr,tpr)