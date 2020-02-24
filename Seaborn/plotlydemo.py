#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:15:56 2019

@author: student
"""

print("Hello world:")
# importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as go
df=pd.read_csv('http://rawgihubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas=df[(df.continent=='Americas')]
europe=df[(df.continent=='Europe')]
# create one graph 
trace_comp0=go.Scatter(
        x=americas.gdp_percap,
        y=americas.life_exp,
        mode='markers',
        markers=dict(size=12,
                     line=dict(width=1),
                     color="navy"
                     ),
        name='Americas',
        text=americas.country,
        )
trace_comp1=go.Scatter(
        x=europe.gdp_percap,
        y=europe.life_exp,
        mode='marker',
        marker=dict(size=13,
                    line=dict(witdh=1),
                    color="red"
                    ),
        name='Europe',
        text=europe.country,
        )
datacomp=[trace_comp0,trace_comp1]
layout=go.Layout(
        title='Life Exceptency vs Percapita GDP',
        hovermode='closest',
        xaxis=dict(
                title='GDP per capita imncome',
                ticklen=5,
                zeroline=False,
                gridwidth=2,
                ),
        yaxis=dict(
                title='Life Excepetency',
                ticklength=5,
                gridwidth=2,
                ),
            )
        
fig_comp=go.Figure(data=datacomp,layout=layout)
py.offline.iplot(fig_comp,filename='life expectency per gdp')