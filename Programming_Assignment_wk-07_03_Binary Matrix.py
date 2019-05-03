# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:49:21 2019

@author: Rajesh D Borate
"""

n,m=(input().split(" "))
n=int(n)
m=int(m)
a=[]
z=[]
for i in range(n):
    l=[]
    for j in range(m):
        l.append(0)
    a.append(l)

for i in range(n):
    o=[int(g) for g in input().split(" ")]
    for j in range(m):
        a[i][j]=o[j]
        z.append(a[i][j])

for i in z:
  if i>1:
    print("NO",end='')
    break
else:
  print("YES",end='')