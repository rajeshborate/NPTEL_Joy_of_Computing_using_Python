# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:19:45 2019

@author: Rajesh D Borate
"""

def endsort(a):
  j=sorted(a)
  n=len(a)
  k=0
  for i in range(n):
    try:
      k=a.index(j[i],k)+1
    except ValueError:
        break
  else:
      i=i+1
  return(n-i)
a=[int(i) for i in input().split(' ')]
print(endsort(a),end='')
