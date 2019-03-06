# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 06:15:26 2019

@author: Rajesh D Borate
"""

k = int(input())

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)