# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:33:19 2019

@author: Rajesh D Borate
"""

def printDict():
    n = int(input())
    d=dict()
    for i in range(1,n+1):
        d[i]=i**2
    print(d)
printDict()