# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:18:44 2019

@author: Rajesh D Borate
"""

s=input()
count=0
count1=0
for i in s:
  if(i.islower()):
    count+=1
  elif(i.isupper()):
    count1+=1
print(count1,count,end="")