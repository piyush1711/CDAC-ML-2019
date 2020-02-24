#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:00:56 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
print(stemmer.stem('working'))

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
print(stemmer.stem('increases'))

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))