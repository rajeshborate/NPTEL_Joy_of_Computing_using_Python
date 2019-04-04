# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:29:53 2019

@author: Rajesh D Borate
"""

import re
ip=input()
l=((re.findall('\d+', ip)))
l=list(map(int,l))
print(max(l),end='')
