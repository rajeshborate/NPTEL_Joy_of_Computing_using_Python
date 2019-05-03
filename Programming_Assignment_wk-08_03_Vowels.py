# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:45:37 2019

@author: Rajesh D Borate
"""

string=str(input(""))
c=0
l=[]
vowels = ('a', 'e', 'i', 'o', 'u')  
for x in string:
    if x not in vowels:
        l.append(x)
        c=0
    else:
        if c==0:
            l.append(x)
            c=c+1
        
            
      
for item in l:
    print(item, end="")
