#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 28

Implement a function that takes as input three variables, and returns the 
largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally
 takes care of for us. All you need is some variables and if statements!

"""

def max_of_three(a, b, c):
    
    '''It gives the maximum number of three numbers'''
    
    if a > b:
        if a > c:
            return a
        else:
            return c
    
    elif b > a:
        if b > c:
            return b
        else:
            return c
    
    elif c > a:
        if c > b:
            return c
        else:
            return b
    
a = max_of_three(3,6,1)
b = max_of_three(4, 2, 7)
c = max_of_three(39, 33, 3)
#print(a)
#print(b)
print(c)
