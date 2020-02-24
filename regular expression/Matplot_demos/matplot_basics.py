#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:39:38 2019

@author: student
"""

import matplotlib.pyplot as plt

#x = [2,3,4,1,6]
#y = [10,12,5,6,7]
#x1 = [3,7,9,2]
#y1 = [12,11,8,5]
#plt.plot(x,y,color="r",label="red label")
#plt.plot(x1,y1,color="b",label="blue label")
#plt.xlabel("x axis")
#plt.ylabel("y axis")
#plt.title("This is title")
#plt.legend()
#plt.grid()


#slices = [7,8,6,11,7]
#activities = ['excercise', 'sleeping','eating','working','playing']
#cols = ['g','c','m','r','k']
#
#plt.pie(slices, labels=activities, colors=cols, startangle=90,shadow=True,explode=(0,0,0.1,0,0))
#plt.title('This is title')
#plt.show()

#days=[1,2,3,4,5]
#sleeping=[7,8,6,11,7]
#eating=[2,3,4,3,2]
#working=[7,8,7,7,2]
#playing=[8,5,7,8,13]
#
#plt.plot([],[],color='m',label='sleeping',linewidth=5)
#plt.plot([],[],color='c',label='eating',linewidth=5)
#plt.plot([],[],color='r',label='working',linewidth=5)
#plt.plot([],[],color='b',label='playing',linewidth=5)
#
#plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])
#plt.xlabel('plot number')
#plt.ylabel('important var')
#plt.legend(loc="upper left")
#plt.title('this is title')
#plt.show()

DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77,32,42]
LABELS=['monday','tuesday','wednesday']
width=0.35
plt.bar(DayOfWeekOfCall,DispatchesOnThisWeekday, width,align='center')
plt.xticks(DayOfWeekOfCall, LABELS, rotation="180")
plt.show()
