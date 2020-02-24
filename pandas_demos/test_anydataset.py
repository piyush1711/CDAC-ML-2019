#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:31:06 2019

@author: student
"""

import numpy as np
import pandas as pd


#df = pd.read_csv("Bollywood_2015.csv")
#df = pd.read_csv("Bollywood_2015.csv", header=None)
#df = pd.read_csv("Bollywood_2015.csv", header=None, names=['Col1','Col2','Col3','Col4'])
#df = pd.read_csv("Bollywood_2015.csv", header=1)
#df = pd.read_csv("Bollywood_2015.csv", skiprows=1)
#df = pd.read_csv("Bollywood_2015.csv", nrows=4)
#df.set_index('Col2',inplace=True)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#df = pd.read_csv("Bollywood_2015.csv", na_values={'BO_Collection':['not available'],'Box_Office_Verdict':['n.a']})

#df = pd.read_csv("Bollywood_2015.csv")
#df1= df.set_index('Budget')
#print(df1)

##df.set_index('Box_Office_Verdict', inplace=True)
##print(df)
#print(df.columns)

#df.reset_index('Box_Office_Verdict', inplace=True)
#print(df.index)
###print(df['Hit'])
#print(df.loc['Hit'])

#df.reset_index('Box_Office_Verdict', inplace=True)
#print(df)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(0)
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna({'BO_Collection':10, 'Box_Office_Verdict':20})
#print(ndf)


#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(method='ffill')
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(method='ffill',limit=2)
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(method='bfill')
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(method='bfill', limit=2)
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.fillna(method='bfill', axis="columns")
#print(ndf)

#df = pd.read_csv("Bollywood_2015.csv", na_values=['n.a', 'not available'])
#ndf = df.interpolate()
#print(ndf)


#def convert_budget(cell):
#    if cell == 'n.a':
#        return 'HI'
#    elif cell == 'not available':
#        return 'Bye'
#    return cell
#    

#df = pd.read_csv("Bollywood_2015.csv")
#df.to_csv('newBoly.csv', index=False)

#df = pd.read_csv("Bollywood_2015.csv", converters={'BO_Collection': convert_budget})
#print(df)

#df = pd.read_excel('stock_data.xlsx')
#print(df)
#
#df.to_excel('myexl.xlsx', index=False)

df = pd.read_csv("Bollywood_2015.csv")
g = df.groupby('Box_Office_Verdict')

for Box_Office_Verdict, data in g:
    print(Box_Office_Verdict)
    print(data)


print("\n\n",g.get_group('Flop'))

print("max: ",g.max())
print("min: ",g.min())
print("mean: ",g.mean())
print("size: ",g.size())
print("count: ",g.count())

g.plot()
