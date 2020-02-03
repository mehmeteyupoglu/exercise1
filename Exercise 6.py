#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or 
not. (A palindrome is a string that reads the same forwards and backwards.)

"""

user_input = input('Enter a word to check whether it is palyndrome:  ')
user_input = user_input.lower()
rvs = user_input[::-1]

if user_input == rvs:
    print('{} is a palyndrome.'.format(user_input.title()))
else:
    print('{} is not a palyndrome.'.format(user_input.title()))

