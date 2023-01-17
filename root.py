#!/usr/bin/env python3nn
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:34:20 2023

@author: soudip
"""
# numerical method to find root using bisection method
function=input("enter a function: ")
print("first provide the interval where the root lies say [i,g] , input i,g ")
i=int(input("enter i = "))
g=int(input("enter g = "))
def f(x):
    return eval(function)

a=float(input("step size: "))
c=0
d=0
f1=f(i)
import numpy as np
for n in np.arange(i,g+a,a):
    if f(n)==0:
        print("the root of the above equation is ",n)
        d+=1
        break
    if f1*f(n)<0:
        c+=1
        break
    else: 
     f1=f(n)
    n=n+a
    n="%0.02f"%n 
if c>0:     
 print("the root is between ","%0.2f"%(n-a)," & ","%0.2f"%n)
if c==0 and d==0:
    print("there is no solution within the range [",i,",",g,"]") 
# another way to define a function is 
#f = lambda x: 10**x + x - 4    
