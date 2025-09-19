#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 22:12:46 2025

@author: mark
"""

# For a given number x determine if it is divisible by another given number y without using the modulo-operator
def divisible(x,y):
    if x==y:
        return True
    if x<y:
        return False
    else:
        return divisible(x-y, y)
    
print(divisible(1200, 2))
print("\n")

# For an array of length 100, and an index x given by the user, calculate the sum of the numbers with index smaller than x
def sum_to_index(A, x, start=0):
    if start==x-1:
        return A[start]
    else:
        return A[start] + sum_to_index(A, x, start + 1)
    
a = range(100)
print(sum_to_index(a, 55))
print("\n")

# For a given number x, determine if it is a prime (a number only divisible by itself and 1)
def is_prime(n, divisor=2):
    if n<=1:
        return False
    if n==2:
        return True
    if n==divisor:
        return True
    elif n%divisor==0:
        return False
    else:
        return is_prime(n, divisor+1)

print(is_prime(653))
print("\n")

# Return the median of a sequence of sorted numbers. 
b = [1,2,3]

def median(A, start=0, end=None):
    if end==None:
        end = len(A) - 1
    # If the list is of even size
    if start==end//2 and len(A)%2==0:
        return (A[start] + A[start+1])/2
    # If the list is of odd size
    elif start==end//2 and len(A)%2!=0:
        return A[start]
    else:
        return median(A, start+1, end)
    
print(median(b))
print("\n")

# Finding the maximum of a sequence without using the max operator
c = [32, 34, 50, 7, 22, 10, 19]

def max_zonder_max(A, current_max=None, start=0, end=None):
    if end==None:
        end = len(A)-1
    if current_max==None:
        current_max = A[start]
    if start==end:
        return current_max
    elif A[start] > current_max:
        current_max = A[start]
        return max_zonder_max(A, current_max, start+1, end)
    else:
        return max_zonder_max(A, current_max, start+1, end)
        
print(max_zonder_max(c))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        