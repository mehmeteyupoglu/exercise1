#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 4

Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. (If you don’t know what a divisor is, it 
is a number that divides evenly into another number. For example, 13 is a 
divisor of 26 because 26 / 13 has no remainder.)

"""

user_input = int(input('Enter a digit to check its divisors:  '))

div = []

for i in range(1, user_input+1):
    if user_input % i == 0:
        div.append(i)
print(div)

"""
One-line code version that gives the same result: 

"""

b = [i for i in range(1, user_input+1) if user_input % i == 0]
print(b)

