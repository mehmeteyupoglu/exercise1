#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 11

Ask the user for a number and determine whether the number is prime or not. 

"""

user_input = int(input('Enter a number to check whether it is a prime number. '))

def check_primality(num):
    '''Returns true if it is prime, returns false otherwise'''
    
    if num == 1:
        prime = False
    
    elif num == 2:
        prime = True
    
    else:
        prime = True
        
        for i in range(2, (num//2)+1):
            if num % i == 0:
                prime = False
                
    return prime

a = check_primality(user_input)

print(a)