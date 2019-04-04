# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:29:53 2019

@author: Rajesh D Borate
"""
a = int(input())
mat=[]
for i in range(0,a):    
    l = list(map(int, input ().split ()))
    mat.append(l)
m=a
n=a
k = 0
l = 0 
count = 0 
total = a*a
  
while (k < m and l < n) : 
    if (count == total) : 
        break
  
    for i in range(k, m) : 
        print(mat[i][l], end = " ") 
        count += 1
          
    l += 1
  
    if (count == total) : 
        break
         
    for i in range (l, n) : 
        print( mat[m - 1][i], end = " ") 
        count += 1
          
    m -= 1
          
    if (count == total) : 
        break
   
    if (k < m) : 
        for i in range(m - 1, k - 1, -1) : 
            print(mat[i][n - 1], end = " ") 
            count += 1
    n -= 1
  
    if (count == total) : 
        break
           
    if (l < n) : 
        for i in range(n - 1, l - 1, -1) : 
            print( mat[k][i], end = " ") 
            count += 1
                  
    k += 1