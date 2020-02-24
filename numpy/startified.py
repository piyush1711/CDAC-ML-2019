#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:00:59 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import  model_selection,datasets

df_iris=datasets.load_iris()
#print(df_iris)
features=df_iris.data[:,:2]
labels=df_iris.target
df_labels=pd.DataFrame(labels)
print(df_labels[0].value_counts())
x_train,x_test,y_train,y_test=model_selection.train_test_split(features,labels,test_size=0.2,stratify=labels)
df_ytest=pd.DataFrame(y_test)
df_ytrain=pd.DataFrame(y_train)
print(df_ytrain[0].value_count())
print(df_ytest[0].value_c
