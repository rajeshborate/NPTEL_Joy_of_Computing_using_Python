# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 05:17:54 2019

@author: Rajesh D Borate
"""
a=str(input())

n1=0
n2=0

for c in a:
    if(c=='1'):
        n1+=1
    if(c=='0'):
        n2+=1

if(n1==1 or n2==1):
    print("YES")
else:
    print("NO")        
