# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:21:47 2019

@author: Rajesh D Borate
"""

n=int(input())
for n in range(1,n+1):
    if(n%3==0 and n%5==0):
        print(n,"=FizzBuzz")
    elif(n%3==0):
        print(n,"=Fizz")
    elif(n%5==0):
        print(n,"=Buzz")
    else:
        print(n)