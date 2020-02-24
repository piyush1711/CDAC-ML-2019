#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:14:47 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))

stemmer1 = PorterStemmer()
print(stemmer1.stem('increases'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('incresases'))