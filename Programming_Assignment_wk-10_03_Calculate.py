# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:36:55 2019

@author: Rajesh D Borate
"""

d=[int(i) for i in input().split(",")]
c=50
h=30
l=len(d)
f=[]
for i in range(l):
    q=((2 * c * d[i])/h)**(0.5)
    f.append(round(q))
for i in range(l):
  if i==l-1:
    print(f[i],end="")
  else:
    print(f[i],end=',') 