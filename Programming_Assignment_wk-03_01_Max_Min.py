# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 05:17:54 2019

@author: Rajesh D Borate
"""
a=[int(x) for x in input().split()]

b=[]

for i in a:
    i=int(i)
    if(i%3!=0):
        b.append(i)

print(b)
