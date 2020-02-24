#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:48:39 2019

@author: student
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Loadinng the data
#tips=sns.load_dataset("tips")
##Crating violine Plot (here x is defining the color)
#sns.violinplot(x="tip",data=tips)
##showing the plot
#plt.show() 

#data Set available on "https://github/mwaskon/seaborn-data"
#Load Iris Data
#iris=sns.load_dataset("iris")
#
##construct iris p;ot
#sns.swarmplot(x="species",y="petal_length",data=iris)
#plt.show()

#
#titanic=sns.load_dataset("titanic")
#g=sns.factorplot("class",'survived','sex',data=titanic,kind="bar",palette="colorblind",legend=False)
#plt.show()


from matplotlib.colors import ListedColormap
#N = 500
#current_palette=sns.color_palette("dark",n_colors=5)
#cmap=ListedColormap(sns.color_palette(current_palette).as_hex())
#print(type(cmap))
##Initializing the data
#
#data1=np.random.randn(N)
#data2=np.random.randn(N)
#
#colors=np.random.randint(0,5,N)
#plt.scatter(data1,data2,c=colors,cmap=cmap)
#plt.colorbar()
#plt.show()




#########################################3
#iris=sns.load_dataset("iris")
#tips=sns.load_dataset("tips")
#
#with sns.axes_style("white"):
#    plt.subplot(2,1,figsize=(8,4))
#    plt.subplot(212)
#    sns.swarmplot(x="species",y="petal_length",data=iris)
#
#plt.subplot(211) # 211 meansa 2 rows 1 colum 1st figure
#sns.violinplot(x="total_bill",data=tips)
#plt.show()

fake=pd.DataFrame({'cat':['red','green','blue'],'val':[1,2,3]})
ax=sns.barplot(x='cat',y='val',color="black",data=fake)
ax.set(xlabel="commonxlabel",ylabel="commonylabel")
plt.show()