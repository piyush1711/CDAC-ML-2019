#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:55:15 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("off_stationary.csv",names=['id','product'])
    
table=pd.pivot(dataset,index='id',values='product',columns='product')

