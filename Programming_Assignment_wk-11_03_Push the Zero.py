# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:32:51 2019

@author: Rajesh D Borate
"""

def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

num_list = list(map(int, input ().split ()))

res = move_zero(num_list)

for i in range(len(res)):
    if(i==len(res)-1):    
        print(res[i],end="")
    else:
        print(res[i],end=" ")