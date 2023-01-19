##!/usr/bin/env python3nn
## -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 11 17:34:20 2023
#
#@author: soudip
#"""
## numerical method to find root using tabular method

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
    
 #newton raphson method
 
import numpy as np
import math
def f(x):
  return 10**x + x - 4
def df(x):
  return math.log(10)*10**x+1
a=float(input("enter the intital guess of the root :"))
i=abs(f(a)/df(a))
x=a
while i>0.001:
    x=x-i
    i=abs(f(x)/df(x))
print("%0.3f"%x)

#bisection method

import numpy as np
import math
function=input("enter a function: ")
def f(x):
  return eval(function)
print("first provide the interval where the root lies say [i,g] , input i,g ")
i=int(input("enter i = "))
g=int(input("enter g = "))
er=float(input("enter the tolerable error : "))
mid=(i+g)/2
while abs(i-g)>er:
    if f(i)*f(mid)<0:
        i=i
        g=mid
    else:
        i=mid
        g=g
    mid=(i+g)/2   
print("the root lies between ",i," and ",g)
        
    
    
    




