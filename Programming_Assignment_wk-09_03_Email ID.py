# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:28:34 2019

@author: Rajesh D Borate
"""

ip=input()
x=ip.index("@")
print(ip[x+1:len(ip)-4],end='')