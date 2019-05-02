# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:35:20 2019

@author: Rajesh D Borate
"""

ip=input()
l=['0','1','2','3','4','5','6','7','8','9',' ']
for i in range(65,90):
  l.append(chr(i))
for i in range(97,122):
  l.append(chr(i))
for i in ip:
  if i not in l:
    print("YES",end='')
    break
else:
  print("NO",end='')