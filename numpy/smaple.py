#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:33:33 2019

@author: student
"""
import numpy as np
import pandas as pd

#
#data=pd.read_csv("/home/student/Desktop/old data/python/python/dataset/aapl.csv")
#print(data)
#datasmaple=data.sample(n=11,replace="False")
#print(datasmaple)
#skip_idx=[x for x in range(1,data.shape[0]) if x % 2 != 0]
#print(skip_idx)
skipped=pd.read_csv("/home/student/Desktop/old data/youtubedata.csv",skiprows=lambda x: x %5 !=0)
print(skipped[1:].mean()) 

# 1135       958.444169
#252        237.414392
#1075    319060.029777
#4.96         3.696179
#46         824.168734
#86         712.382134
#dtype: float64   
#1135       958.930779
#252        226.437577
#1075    227971.751545
#4.96         3.769271
#46         613.197775
#86         509.501854
#dtype: float64