#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:31:12 2019

@author: student
"""

# Numpandas all functions Trail & Error:
#import numpy as np
import pandas as ps
 Without Header Relacing n.a with NAN
appl=ps.read_csv("/home/student/Desktop/old data/python/python/dataset/aapl.csv",na_values=["n.a","not available"])
 Read With Header 
appl=ps.read_csv("/home/student/Desktop/old data/python/python/dataset/aapl.csv",header=1)
Reading with  New Column Names
appl=ps.read_csv("/home/student/Desktop/old data/python/python/dataset/aapl.csv",header=1,names={'Col1','Col2','Col3','Col4','Col','Col6'})
print(appl)
Return Info about file data
print(appl.info())
return Column Names
print(appl.columns)
print(appl[1:11])
#TO change the format of date
appl=ps.read_csv("/home/student/Desktop/old data/python/python/dataset/aapl.csv",na_values=["n.a","not available"],parse_dates=['Date'])
#print(appl)
# Will Print High Columns as Index
#print(appl.set_index('High',inplace=True))
# Will Return Index column only
#print(appl.index)
# will fill the all the forward cell with the values by next value
#pdf=appl.fillna(method="ffill")
# will fill the all the backward cell with the values by next value with limit and limit should be always greater than 1
pdf=appl.fillna(method="bfill",limit=2)
#print(pdf)
 WIll fill na values with (0)
ndf=appl.fillna(0)
print(ndf)
jaha na values hai uske upper aur niche wale values ke bich wali values fill karta hai "interpolate()"
inter=appl.interpolate()
print(inter)
g=appl.groupby('Date')
for i in g:
    print(i[0])
print(g.count())
print(g.size())
print(g.describe())


def grouper(df,idx,col):
    if 96.75 <= df[col].loc[idx] <= 100.00:
        return '96.75-100.00'
    elif 110.00 <= df[col].loc[idx] <= 140.00:
        return '120.24-100.00'
    else:
        return 'others'
    
g1=appl.groupby(lambda x:grouper(appl,x,'High'))
#for j in g1:
#    print(j[1])
for key,d in g1:
    print("Group by key:{}{}".format(key,d))
    print("--------------")
    print(d[1:14])
#print("Min",g1[])

