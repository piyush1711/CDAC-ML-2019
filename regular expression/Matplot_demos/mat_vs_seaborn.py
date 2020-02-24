#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:49:37 2019

@author: student
"""

#import matplotlib.pyplot as plt
#import pandas as pd
#
#fig, ax= plt.subplots()
#
#tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
#ax.violinplot(tips["total_bill"], vert=False)
#plt.show()



#import matplotlib.pyplot as plt
#import seaborn as sns
#
#tips = sns.load_dataset("tips")
#sns.violinplot(x="total_bill", data=tips)
#plt.show()


#import matplotlib.pyplot as plt
#import seaborn as sns
#
#iris = sns.load_dataset("iris")
#sns.swarmplot(x="species", y="petal_length", data=iris)
#plt.show()


#import matplotlib.pyplot as plt
#import seaborn as sns
#
#titanic = sns.load_dataset("titanic")
#
#g = sns.factorplot("class","survived","sex",data=titanic,kind="bar", palette="muted", legend=False)
##sns.factorplot("class","survived","sex",data=titanic,kind="bar", palette="muted", legend=False)
#plt.show()

#import seaborn as sns
#import matplotlib.pyplot as  plt
#import numpy as np
#from matplotlib.colors import ListedColormap
#
##Define n
#N = 500
#
##construct colormap
#current_palette = sns.color_palette("dark", n_colors = 5)
#cmap = ListedColormap(sns.color_palette(current_palette).as_hex())
#print(type(cmap))
#
##init the data
#data1 = np.random.randn(N)
#data2 = np.random.randn(N)
#
## assume there are 5 possible lables
#colors = np.random.randint(0,5,N)
#
##create scatter plot
##cmap is optional if given will be used must be ListedColormap object
#plt.scatter(data1, data2, c=colors, cmap=cmap)
#
##Add color bar
#plt.colorbar()
#
#plt.show()


#import seaborn as sns
#import matplotlib.pyplot as plt
#
#iris = sns.load_dataset("iris")
#tips = sns.load_dataset("tips")
#
##set axes to white for first subplot
#with sns.axes_style("white"):
#    plt.subplot(211)
#    sns.swarmplot(x="species", y="petal_length", data=iris)
#    
##init 2nd subplot
#plt.subplot(212)
#sns.violinplot(x="total_bill", data=tips)
#plt.show()


#3 figures
#import seaborn as sns
#import matplotlib.pyplot as plt
#
#iris = sns.load_dataset("iris")
#tips = sns.load_dataset("tips")
#titanic = sns.load_dataset("titanic") 
#
##set axes to white for first subplot
#with sns.axes_style("white"):
#    #211 means 2 rows 1 column 1st figure
#    plt.subplot(311)
#    sns.swarmplot(x="species", y="petal_length", data=iris)
#    plt.subplot(312)
#    sns.violinplot(x="total_bill", data=tips)
#    
##init 2nd subplot
#plt.subplot(313)
#sns.violinplot(x="total_bill", data=tips)
##sns.factorplot("class","survived","sex",data=titanic,kind="bar", palette="muted", legend=False)
#plt.show()

###check
#import seaborn as sns
#import matplotlib.pyplot as plt
#
#iris = sns.load_dataset("iris")
#tips = sns.load_dataset("tips")
#
#
#plt.subplot(1,2,figsiz=(8,4))
#sns.swarmplot(x="species", y="petal_length", data=iris)
#sns.violinplot(x="total_bill", data=tips)
#plt.show()

##set axes to white for first subplot
##with sns.axes_style("white"):
##    plt.subplot(211)
##    sns.swarmplot(x="species", y="petal_length", data=iris)
##    
###init 2nd subplot
##plt.subplot(212)
##sns.violinplot(x="total_bill", data=tips)
##plt.show()

#
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd
#
#fake = pd.DataFrame({'cat':['red','green','blue'], 'val':[1,2,3]})
##ax = sns.barplot(x='val', y='cat', data=fake,color='black')
#ax = sns.barplot(x='cat', y='val', data=fake,color='black')
##plt.xlabel('common xlabel')
##plt.ylabel('common ylabel')
#ax.set(xlabel="common xlabel", ylabel="common ylabel", title='some title')
##ax.get_xticklabels() this is required bcoz of string labels
#ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
#plt.show()


import plotly
print(plotly.__version__)


