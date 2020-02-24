#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:38:42 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


mydata=pd.read_table("http://bit.ly/chiporders")
print(mydata.columns)
print(mydata.shape)
print(mydata.head(15))

print(mydata.loc[1:5,"item_name"])

df = mydata.loc[(mydata["item_name"]=="ChickenBowl"),["item_name","quantity"]]
print("----------")
print(df)
print("---------------")
qnt=mydata.loc[(mydata["quantity"]>1)]
print(qnt)






mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.columns)

print(mymoviedata.head(15))
print(mymoviedata.tail(15))
print(mymoviedata.iloc[1:5,2])
print(mymoviedata.loc[1:5,1])
print(mymoviedata.info())
print(mymoviedata.describe())
#poi=mymoviedata.loc[(mymoviedata[1]>20 and mymoviedata[3]=="technician"),[1,3]]
#print(poi)

#mymoviedata["job_length"]=mymoviedata["job"].map(lambda x:len(x))

dummy_data2={'id':['2','8','6','6','7'],
             'feature1':['A','B','C','h','k'],
             'feat2':['p','l','j','e','z']
             }
df1=pd.DataFrame(dummy_data2,columns=['id','feature1','feat2'])
print(df1)
#pf1['dept']='sales'
#pf2['dept']='Purchase'
## =============================================================================
# comined=pd.concat([pf1,pf2])
# =============================================================================
# =============================================================================
# print(combined)
# =============================================================================








dummy_data3 = {
        'id':['1','2','3','4','5','6','7','8','9','10','11'],
        'Feature3':[12,13,14,15,16,17,18,19,20,14,18]
        }
df3=pd.DataFrame(dummy_data3,columns=['id','Feature3'])
print(df3)




group = mymoviedata.groupby(3)
print(group.get_group("technician")) # give all the rows having technician
print(group.get_group("technician"))
print(mymoviedata[3].unique()) # gives unique data







































