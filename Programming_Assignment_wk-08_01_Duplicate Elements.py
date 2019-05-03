# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:43:05 2019

@author: Rajesh D Borate
"""

s=[int(x) for x in input().split()]
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    print(i, end=" ")
