#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:32:18 2019

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

d = {}
from sklearn.model_selection import cross_val_score

#####1
from sklearn.tree import DecisionTreeClassifier
classifier1=DecisionTreeClassifier(criterion='entropy',random_state=0)
#classifier4.fit(X,Y)

score1=cross_val_score(classifier1,X,Y,cv=5)
avg1=np.average(score1)
print("Decesion Tree Score:",avg1)

d["Decesion Tree Score:"] = avg1


######2
from sklearn.ensemble import RandomForestClassifier
classifier2=RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
#classifier5.fit(X,Y)

score2=cross_val_score(classifier2,X,Y,cv=5)
avg2=np.average(score2)
print("Random Forest Score:",avg2)

d["Random Forest Score:"] = avg2


######3
from sklearn.neighbors import KNeighborsClassifier
classifier3=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
#classifier6.fit(X1,Y)

from sklearn.model_selection import cross_val_score
score3=cross_val_score(classifier3,X,Y,cv=5)
avg3=np.average(score3)
print("KNN Score:",avg3)
d["KNN Score:"] = avg3


######4
from sklearn.naive_bayes import GaussianNB
classifier4=GaussianNB()
#classifier7.fit(X,Y)

from sklearn.model_selection import cross_val_score
score4=cross_val_score(classifier4,X,Y,cv=5)
avg4=np.average(score4)
print("Naive Bays Score:",avg4)

d["Naive Bays Score:"] = avg4


#######5
#Fitting Naive Byes to the Training set
from sklearn.naive_bayes import BernoulliNB
classifier5=BernoulliNB()
#classifier.fit(X,Y)

from sklearn.model_selection import cross_val_score
score5=cross_val_score(classifier5,X,Y,cv=5)
avg5=np.average(score5)
print("Bernoulli Naive Bays Score:",avg5)

d["Bernoulli Naive Bays Score:"] = avg5

m = max(d.values())

for i in d.items():
    if i[1] == m:
        print('-------------------------------------------------------')
        print(i[0],i[1],"Is the best model")



