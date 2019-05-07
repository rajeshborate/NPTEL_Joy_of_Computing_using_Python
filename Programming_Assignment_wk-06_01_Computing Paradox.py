# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:30:44 2019

@author: Rajesh D Borate
"""

n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
key=a[k-1]
a.sort()
for i in range(len(a)):
    if key==a[i]:
        print(i+1)
        break