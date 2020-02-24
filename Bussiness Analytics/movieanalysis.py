#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:25:03 2019

@author: student
"""
import numpy as np
import pandas as pd
movie=pd.read_csv("movies.csv")
#print(movie['genres'])
lst=['Action','Comedy','Romance','Thriller']
lst2=[]
moviecolumns=movie[['genres','title']]
#print(moviecolumns)
str1=movie.genres.astype(str)
a=movie.genres.str.split('|')#.str.get(1)
u=0
movie['splitted']=a
print(movie['splitted'])
a=0
b=0
c=0
d=0
for j in movie['splitted']:
    if lst[0] in j:
       a=a+1
    elif lst[1] in j:
       b=b+1
    elif lst[2] in j:
        c=c+1
    elif lst[3] in j:
        d=d+1
print(a,b,c,d)

dict2={}

   
    











































#i=0
#c=0
#for j in movie['genres']:
#    if lst[c] in j:
#        print(j)
#        i=i+1        
#    if lst[c+1] in j:
#        print(j)
#        i=i+1
       
#    print(i)
#        c=c+1
            
            
            #            if c > 4:
#                break

#for i in genres:
#    if i[0]=="Action|Comedy|Romance|Thriller":
#        print("MASALA MOVIES")
#        print(i[1]['title'])




#
#for j in movie['genres']:
#    j.split("\\|")
#     print(j)
