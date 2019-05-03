# -*- coding: utf-8 -*-
"""
Created on Fri May  3 05:44:37 2019

@author: Rajesh D Borate
"""

import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
  
string = input("")
if(ispangram(string) == True): 
    print("YES", end="") 
else: 
    print("NO", end="") 
