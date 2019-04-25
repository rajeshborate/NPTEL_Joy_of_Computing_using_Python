# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:17:25 2019

@author: Rajesh D Borate
"""

s=input()
#s.replace(".",x)
alpha="abcdefghijklmnopqrstuvwxyz"
for i in alpha:
  t=s.replace(".",i) #dont use s only as in the else statement 
  if(t==t[::-1]):
    print(t,end="")
    break
else:
  print("-1",end="")