#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:09:24 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
set2=set()
lst=[]
# str2=input("enter the genre  you want:")
data_movies=pd.read_csv(r"/home/student/Desktop/old data/python/python/dataset/movies.csv")
# print(data_movies['genres'].value_counts())
data_movies.genres=data_movies.genres.str.split('|')
#ratings=pd.read_csv(r"C:\Users\lokesh\Downloads\ml-latest-small\ratings.csv")
dta=data_movies.assign(genres1=data_movies.genres).explode('genres1')
#print(dta.head(20))
value=dta['genres1'].value_counts()

print(value)
#merged=pd.merge(data_movies,ratings,on='movieId')
df=pd.DataFrame(value)
# print(df['genres'])


#for j in np.split(df,2):
#    print(j)
# plt.figure(figsize=(10,10))
# plt.rcParams['patch.force_edgecolor'] = True
#df['genres'].hist(bins=100)
#plt.show()
# plt.bar(value,height=34,align='center')
# plt.show()
# movies=data_movies.explode(movies,['genres'])
# print(movies.head())
# count=0
# print(data_movies['split'])
# for j in data_movies['split']:
#     if str2.capitalize() in j:
#         count=count+1
# print(count)
# print(ratings.head())
# merged=pd.merge(data_movies,ratings,on='movieId')
# print(merged.head())