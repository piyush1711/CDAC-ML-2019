#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:09:37 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#importing datset
#quoting=3 will ignore " character 
dataset= pd.read_csv(r'/home/student/Desktop/Data_Aug2019/Python/Programs/NLP/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)


#cleaning the text
import re
import nltk

#stopword is a package that contains list of words in different columns
nltk.download('stopwords')
from nltk.corpus import stopwords

#this class stores trees of similar words
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review=review.lower()
    #will split by default at \t
    review = review.split()
    
    ps=PorterStemmer()
    #ps.stem will do steming means will store only root of words
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    
    
# Creating Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)  ## here we are limitng the column to 1500 of different words so here there will be loss of data 
X=cv.fit_transform(corpus).toarray()
Y=dataset.iloc[:,1].values

#splitting the datset into training and testing set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
#print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

truePositive=cm[1,1]
falsePositive=cm[0,1]
trueNegative=cm[0,0]
falseNegative=cm[1,0]

print("Random Forest")
#accuracy
totalTrue=truePositive+trueNegative
#print(totalTrue)
total=cm.sum()
#print(total)
accuracy=totalTrue/total
print("Accuracy : ",accuracy)

#precesion
precesion=truePositive/(truePositive+falsePositive)
print("Precesion : ",precesion)

#recall
recall=truePositive/(truePositive+falseNegative)
print("Recall : ",recall)

#f1score
f1score=(2*precesion*recall)/(precesion+recall)
print("F1-Score : ",f1score)

print("-----------------------------------------------------")