#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:06:10 2019

@author: student
"""

"""
1. Complete following program
import pandas as pd
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
# add headings to the column- col1,col2,col3,col4,col5
#display only column col3
#add col6 concatenate values of col2 and col3 and seperate them by :
# retrieve values of col1 and col4 display bar graph
# display names of all the columns.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#nam=['col1','col2','col3','col4','col5']
#
#mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None,names=nam)
## add headings to the column- col1,col2,col3,col4,col5
#print(mymoviedata.columns)
##display only column col3
#print(mymoviedata['col3'])
##add col6 concatenate values of col2 and col3 and seperate them by :
#mymoviedata['col6']=mymoviedata['col2'].apply(str)+":"+mymoviedata['col3']
#print(mymoviedata['col6'])
## retrieve values of col1 and col4 display bar graph
#plt.bar(mymoviedata['col1'],mymoviedata['col4'],align='center')
#plt.show()
## display names of all the columns.
#print(mymoviedata.columns)


"""
create a list for storing year 2010 to 2014
create a list for each year for storing sales amout for of 5 products in each years
draw pie chart and stack graph to compare sales
"""
df=pd.read_csv("/home/student/Desktop/python/dataset/sales.csv")


col=['r','g','b','c','k']
#year2=list(set(df['year']))
#print(year2)
group=df.groupby(df['year'])
for j in group:
    print(j[0])
max1=group['sales'].max()
#plt.pie(max1,colors=col,labels=max1,startangle=90)
#year2=group['year'].unique()
plt.show()
df[1].groupby('product')['sales'].mean()
for i ,j in group:
    print(i)
    li=j.groupby('product')['sales'].mean()
    print(li)
    
product3=df['product'].unique()
plt.pie(li,colors=col,labels=year2)