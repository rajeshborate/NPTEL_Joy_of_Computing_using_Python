# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:15:35 2019

@author: Rajesh D Borate
"""

a,b1,b2=map(int,(input().split()))
cab=(2*a)/b2
walk=(1.414*a)/b1
if walk<cab:
  print("Walk",end="")
else:
  print("Cab",end="")