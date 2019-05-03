# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:48:06 2019

@author: Rajesh D Borate
"""

n=int(input())
a=[]
z=[]
for i in range(n):
    l=[]
    l2=[]
    for j in range(n):
        l.append(0)
        l2.append(0)
    a.append(l)
    z.append(l2)

for i in range(n):
    o=[int(g) for g in input().split(" ")]
    for j in range(n):
        a[i][j]=o[j]
for i in range(n):
    for j in range(n):
        z[i][j]=a[j][i]
if (z==a):
    print("YES",end='')
else:
    print("NO",end='')