# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:30:45 2019

@author: Rajesh D Borate
"""

import sys; 
  

def findMinDiff(arr, n, m): 
  
    # if there are no chocolates or number 
    # of students is 0 
    if (m==0 or n==0): 
        return 0
  
    # Sort the given packets 
    arr.sort() 
  
    # Number of students cannot be more than 
    # number of packets 
    if (n < m): 
        return -1
  
    # Largest number of chocolates 
    min_diff = sys.maxsize 
  
    # Find the subarray of size m such that 
    # difference between last (maximum in case 
    # of sorted) and first (minimum in case of 
    # sorted) elements of subarray is minimum. 
    first = 0
    last = 0
    i=0
    while(i+m-1<n ): 
      
        diff = arr[i+m-1] - arr[i] 
        if (diff < min_diff): 
          
            min_diff = diff 
            first = i 
            last = i + m - 1
          
        i+=1
          
    return (arr[last] - arr[first])

n,m = input().split(' ')
n = int(n)
m = int(m)

A = [int(i) for i in input().split(" ")]

print(findMinDiff(A, n, m))