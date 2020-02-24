#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:36:17 2019

@author: student
"""
import pandas as pd
import numpy as np


mydata=pd.read_table("/home/student/Desktop/Data_Aug2019/Python/Data/python/dataset/Chiporder.dat")
print(mydata.columns)
print(mydata.shape)
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.columns)
print(mymoviedata.shape)
print(mymoviedata.head())
print(mymoviedata.head(15))
print(mymoviedata.tail())
print(mymoviedata.tail(15))
lst=["movie_id","reviews","gender","job","views"]
mymoviedata.columns=lst

print(mymoviedata.iloc[1:5,2:4])
print(mymoviedata.loc[1:5,["gender","job"]])

df = mymoviedata.loc[(mymoviedata["gender"]=="M"),["job","gender"]]
print(df)

#print(mymoviedata.loc[(mymoviedata[["views"]].astype(int)>=32000),["job","gender","views"]])

print(mymoviedata.info())

print(mydata.loc[(mydata["quantity"]>1),["quantity","item_name"]])

print(mymoviedata.describe())

#a=mymoviedata.loc[(mymoviedata["reviews"]>20 and mymoviedata["job"]=="technician"),["job","reviews","gender"]]
#print(mymoviedata.loc[(mymoviedata["views"].astype(str).astype(int)>32000 and mymoviedata["job"]=="technician"),["job","reviews","gender"]])
mymoviedata["job_length"]=mymoviedata["job"].map(lambda x:len(x))


d1 = {'id':['1','2','3'], 'feature1':['A','B','C'], 'feature2':['D','E','F']}
print(d1)
df1=pd.DataFrame(d1, columns=['id','feature1','feature2'])
print(df1)

d2 = {'id':['4','5','6'], 'feature1':['AA','BB','CC'], 'feature2':['DD','EE','FF']}
df2=pd.DataFrame(d2, columns=['id','feature1','feature2'])
print(df2)
df3 = pd.concat([df1,df2])
print(df3)
df3 = pd.concat([df1,df2],ignore_index=True)
print(df3)
d4 = {'id':['1','2','8'], 'feature3':['AAA','BBB','CCC']}
df4 = pd.DataFrame(d4, columns=['id','feature3'])
print(df4)

mergedf = pd.merge(df3,df4,on='id')
print(mergedf)


gr_ob = mymoviedata.groupby('job')
print(gr_ob)

#gr_ob_count = mymoviedata.groupby('job')['job'].count()
gr_ob_count = mymoviedata.groupby('job')['job'].first()
print(gr_ob_count)

print(gr_ob.get_group('technician'))

print(mymoviedata["job"].unique())



Data={'Product':['AAA','BBB','CCC'],'Price':['210','250','22XYZ']}

df=pd.DataFrame(Data)
df['Price']=pd.to_numeric(df['Price'],errors='coerce')

print(df)
print(df.dtypes)

df=df.replace(np.nan,0,regex=True)
df['Price']=df['Price'].astype(int)

print(df)
print(df.dtypes)



data={'name':['Jason','Molly','Tine','Jake','Amy'],'year':[2012,2012,2013,2014,2014],'reports':[4,24,31,2,3]}
df=pd.DataFrame(data,index=['Cochice','Pima','Santa Cruz','Maricopa','Yuma'])
print(df)


df1=df.drop(['Cochice','Pima'])
print(df1)

df2 = df.drop('reports', axis=1)
print(df2)

df3 = df.drop(df.index[-2])
print(df3)

