# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 06:17:26 2019

@author: Rajesh D Borate
"""

from random import randint
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

sorted = True

while(sorted):
    j = randint(0,n-1)
    i = randint(0,n-1)
    arr[i],arr[j] = arr[j],arr[i]
    for k in range(0,n-1):
        if (arr[k] > arr[k+1]):
            sorted = False
    
    if(sorted):
        break
    else:
        sorted = True

for i in range(n):
    if(i==n-1):
        print(arr[i])
    else:
        print(arr[i],end=" ")