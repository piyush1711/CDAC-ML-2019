#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:18:35 2019

@author: student
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:16:57 2019

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

dataset=pd.read_csv("Social_Network_Ads.csv")
x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)


def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color='orange',label='ROC')
    plt.plot([0,1],[0,1],color='darkblue',linestyle='--')
    plt.xlabel('FalsePositiveRate')
    plt.ylabel('TruePositiveRate')
    plt.title("KNN -Reciver Operaring Characterstics(ROC) Curve")
    plt.legend()

#Step4:Split the data into train & test
trainx,testx,trainy,testy=train_test_split(x_train,y_train,test_size=0.3,random_state=1)
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