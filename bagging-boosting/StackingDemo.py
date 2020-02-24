#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:20:15 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.model_selection import StratifiedKFold
def Stacking(model,train,y,test,n_fold):
    folds=StratifiedKFold(n_splits=n_fold,random_state=1)
    test_pred=np.empty((test.shape[0],1),float)
    train_pred=np.empty((0,1),float)
    
    for train_indices,val_indices in folds.split(train,y.values):
        x_train,x_val=train.iloc[train_indices],train.iloc[val_indices]
        y_train,y_al=y.iloc[train_indices],y.iloc[val_indices]
        
        model.fit(X=x_train,y=y_train)
        train_pred=np.append(train_pred,model.predict(x_val))
        test_pred=np.append(test_pred,model.predict(test))
    return test_pred.reshape(-1,1),train_pred


#Step1 : create dataset
    
X,y = make_moons(n_samples=10000,noise=0.5,random_state=0)

#step2: Split the training and test set
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

model1=DecisionTreeClassifier(random_state=1)
x_train=pd.DataFrame(x_train)
y_train=pd.DataFrame(y_train)

test_pred1, train_pred1=Stacking(model=model1,n_fold=10, train=x_train,test=x_test,y=y_train)
train_pred1=pd.DataFrame(train_pred1)
test_pred1=pd.DataFrame(test_pred1)


from sklearn.neighbors import KNeighborsClassifier
model2=KNeighborsClassifier()
x_train=pd.DataFrame(x_train)
y_train=pd.DataFrame(y_train)

test_pred2, train_pred2=Stacking(model=model2,n_fold=10, train=x_train,test=x_test,y=y_train)
train_pred2=pd.DataFrame(train_pred2)
test_pred2=pd.DataFrame(test_pred2)


## create a third model, logistic regression on the predictions
#of the decision tree and knn models

df=pd.concat([train_pred1,train_pred2],axis=1)
df_test=pd.concat([test_pred1,test_pred2],axis=1)


x=df.iloc[:,:].values
y=y_train.iloc[:,0].values

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x,y)
y_test=model.predict(df_test)
print("Score : ",model.score(df_test,y_test))
#print("Accuracy Score : ",accuracy_score())














