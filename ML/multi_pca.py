#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:30:25 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Default.csv")
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
dataset['default']=label.fit_transform(dataset['default'])
dataset['student']=label.fit_transform(dataset['student'])

x=dataset.iloc[:,1:].values
y=dataset.iloc[:,0].values

 
