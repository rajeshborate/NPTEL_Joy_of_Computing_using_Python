# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:36:01 2019

@author: Rajesh D Borate
"""

ip=int(input())
x=ip%6
if x==0 or x==1 or x==3:
  print("YES",end="")
else:
  print("NO",end="")