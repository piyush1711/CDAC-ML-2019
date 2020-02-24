import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())

mycol = ['Sr.No.','Age','Gender','Profession','Views']
mymoviedata.columns = mycol
print(mymoviedata.head())

#display col3
print(mymoviedata['Gender'])

#concate two column
mymoviedata['col6'] = mymoviedata['Age'].apply(str)+':'+mymoviedata['Gender']
print(mymoviedata['col6'])


age=mymoviedata['Age'].unique()
profession=mymoviedata['Profession'].unique()
print(profession)
print(age)
mymoviedata['Views']=pd.to_numeric(mymoviedata['Views'],errors='coerce')


###graph1
g=mymoviedata.groupby('Age')
avg=g['Views'].mean()
print(avg)
plt.bar(age,avg,align='center')
plt.show()


###graph2
l=mymoviedata.groupby('Profession')
avg1=l['Views'].mean()
print(avg1)
plt.bar(profession,avg1,align='center')
plt.xticks(profession,rotation="90")
plt.show()
