# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:15:41 2019

@author: Rajesh D Borate
"""

s=input()
count=0
for i in s:
  if(i=="A" or i=="D" or i=="O" or i=="P" or i=="R"):
    count+=1
  elif(i=="B"):
    count+=2
print(count,end="")