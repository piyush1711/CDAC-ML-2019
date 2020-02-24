#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:03:47 2019

@author: student
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing the Data
dataset=pd.read_csv("/home/student/PycharmProjects/helloworld/venv/lib64/python3.5/site-packages/All DataSets/Social_Network_Ads.csv")
x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


#classifier=LogisticRegression(random_state=0)
#classifier.fit(x_train,y_train)
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(x_train,y_train)

##Predicting the Test set Result
y_pred=classifier.predict(x_test)


##Making Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


#K-Fold Cross Validaion
from sklearn.model_selection import cross_val_score
score=cross_val_score(estimator = classifier,x=x_train,y=y_train,cv=10)
print(score.mean())

from sklearn.model_selection import GridSearchCV
parameters=[{'C':[1,10,100,1000],'kernel':['linear']},
             {'C':[1,10,100,1000]}]
grid_search=GridSearchCV(estimator=classifier,
                         param_grid=parameters,
                         scoring='accurary',
                         cv=10,
                         n_jobs=-1)
grid_search=grid_search.fit(x_train,y_train)

best_accuracy=grid_search.best_score_
best_parameters=grid_search.best_params_ 

from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max() +1,step=0.01),np.arange(start=x_set[:,1].min() -1,stop=x_set[:,1].max() +1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))


plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
    
plt.title('Logistioc Regression(training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()