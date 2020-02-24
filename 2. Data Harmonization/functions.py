# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:11:31 2018

@author: ss
"""
import numpy as np

a = np.array([12.4,56.3,29.3,23,9,90.2,45.2,2,90.1])
np.mean(a)
np.std(a)


# Function Definition
def addition(x,y,z):
    f = x+y+z
    return f;

# Function call
addition(3,1,6)

# A function that takes a value and returns its square
def sq_func(x):
    return(x**2)

def mu_sigma(x):
    xbar = np.mean(x)
    s = np.std(x)
    return(xbar,s)

mu_sigma(a) 
mu, sig = mu_sigma(a)
print(mu)
print(sig)
   
def Standardize(x):
    xbar = np.mean(x)
    s = np.std(x)
    stdz = (x - xbar)/s
    return(stdz)
    
print(Standardize(a))   
 
# A lambda function that takes a value and returns its square
sq_lambda = lambda x: x**2

# Use the lambda function
print(sq_lambda(3))

