#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:21:31 2019

@author: student
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:45:41 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('/home/student/Desktop/Restaurant_Reviews.tsv',sep="\t",quoting=3)
import re
import nltk
#stopword is a package that contains list of words in diffrent
nltk.download('stopwords')
from nltk.corpus import stopwords
# this class stores tree of similart words
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    
    
    
    
    #Creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer()
x=cv.fit_transform(corpus).toarray()
y=dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


#fitting Naive Bayes to training Set
from sklearn.naive_bayes import BernoulliNB
burnoli=BernoulliNB()
burnoli.fit(x_train,y_train)


#Predicting the test set reult
y_pred=burnoli.predict(x_test)
#
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
fp=cm[0,1]
fn=cm[1,0]
tn=cm[0,0]
tp=cm[1,1]
total=fp+fn+tn+tp
accuracy=(tp+tn)/total
precision=tp/(tp+fp)
recall=tp/(tp+fn)

f1_score=2*(precision*recall)/(precision+recall)

print(f1_score)

 