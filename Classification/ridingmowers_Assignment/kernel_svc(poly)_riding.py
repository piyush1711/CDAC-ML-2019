#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:11:03 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv("/home/student/Desktop/Data_Aug2019/Python/Programs/Classification/ridingmowers_Assignment/RidingMowers.csv")
X=dataset.iloc[:,[0,1]].values
Y=dataset.iloc[:,2:3].values
#print(X)
#print(Y)

from sklearn.preprocessing import LabelEncoder
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.svm import SVC
classifier=SVC(kernel='poly',degree=3,random_state=0) 
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)
 
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

### visualizing training set
from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
    
plt.title('SVC-Kernel(poly)(Training Set)')
plt.xlabel('Income')
plt.ylabel('Lot-Size')
plt.legend()
plt.show()

#### visualizing testing set
from matplotlib.colors import ListedColormap
x_set,y_set=x_test,y_test
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
    
plt.title('SVC-Kernel(poly)(Test Set)')
plt.xlabel('Income')
plt.ylabel('Lot-Size')
plt.legend()
plt.show()


from sklearn.model_selection import cross_val_score
score1=cross_val_score(classifier,x_train,y_train,cv=5)
print(score1)
print(np.average(score1))



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

trainX,testX,trainy,testy=train_test_split(X,Y,test_size=0.25,random_state=0)
#step 5 fit a model on the train data
model=SVC(probability=True,kernel='poly',degree=3,random_state=0)
model.fit(trainX,trainy)
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