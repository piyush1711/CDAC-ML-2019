#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:22:28 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
startup=pd.read_csv("50_Startups.csv",na_values=['n.a.','not available',0])
startup1=startup.interpolate(method='linear')
x=startup1.iloc[:,0:4].values


print(startup1)
## Imputer 
#impute=Imputer(missing_values='np.nan',strategy='mean',axis=0)
##x=x.reshape(-1,1)
#impute=impute.fit(x[:0:3])
#x[:,0]=impute.transform(x[:0:3])
#print(x)
#




labelencoder_X=LabelEncoder()
x[:,3]=labelencoder_X.fit_transform(x[:,3])

onehotencoder=OneHotEncoder(categorical_features=[3])
x=onehotencoder.fit_transform(x).toarray()
print(x)