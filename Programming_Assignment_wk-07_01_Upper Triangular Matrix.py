# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:46:55 2019

@author: Rajesh D Borate
"""

n=input()
n=int(n)
a=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(0)
    a.append(l)

for i in range(n):
    o=[int(g) for g in input().split(" ")]
    for j in range(n):
        a[i][j]=o[j]

for i in range(n):
    for j in range(n):
        if i>j:
            a[i][j]=0
for i in range(n):
    if(i!=0):
      print( )
    for j in range(n):
        if(j==(n-1)):
            print(a[i][j],end='')
        else:
            print(a[i][j],end=' ')