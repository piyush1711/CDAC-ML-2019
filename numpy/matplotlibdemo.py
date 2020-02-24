#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:38:40 2019

@author: student
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x=[12,15,1,2]
#y=[10,1,17,7]
#
#a=[2,5,6,9]
#b=[13,1,1,19]
#plt.plot(x,y,color="r",label="Test Lable")
#plt.plot(a,b,color="g",label="Test A,b")
#plt.xlabel("x-Axis")
#plt.ylabel("y-Axis")
#plt.title("This is title")
#plt.legend()
#plt.grid()
#
#


#Slics
#slices=[7,1,5,3,6]
#activities=['Exercis','sleepin','eating','working','playing']
#cols=['g','r','b','k','m']
#plt.pie(slices,labels=activities,colors=cols,startangle=90,explode=(0,0,0.1,0,0),shadow=True)
#plt.title('this is pie chart using matlab')
#plt.show()
# Stackpoint


days=[1,2,3,4,5]
sleeping=[3,5,6,7,8]
eating=[5,5,8,3,54]
working=[34,6,6,7,4]
playing=[2,4,2,3,4]
plt.plot([],[],color='m',label="sleeping",linewidth=5)
plt.plot([],[],color='c',label="Eatiing",linewidth=5)
plt.plot([],[],color='r',label="Working",linewidth=5)
plt.plot([],[],color='b',label="Playing",linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])
plt.legend(loc="upper left")
plt.xlabel("plot number")
plt.ylabel("Important Var")
plt.title("This my first in matplotlib graph\nThisis next line")
plt.show()


# Bar Plot
DayOfWeekCall=[1,2,3]
DispatchesOnThisWeekDay=[77,88,99]
LABELS=['monday','tuesday','wednesday']
width=0.45
plt.bar(DayOfWeekCall,DispatchesOnThisWeekDay,width,align="center")
plt.xticks(DayOfWeekCall,LABELS,rotation="80")
#plt.set_xtrick()
plt.show()




#
data={'year':[2010,2011,2012,2011,2012,2010,2011,2012],
      'team':['Bears','Bears','Beras','Packers','Packers','Lions','Lions','Lions'],
      'wins':[12,45,53,53,23,23,42,34],
      'losss':[5,8,6,1,10,6,12]}

print(data['year'])
####################################3333

import pandas as pd
import numpy as np
Data={'Product':['AAA','BBB','CCC'],
      'Price':[190,345,33]}
df=pd.DataFrame(Data)
