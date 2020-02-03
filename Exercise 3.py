#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 3 

Take a list and write a program that prints out all the elements of the list 
that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all 
the elements less than 5 from this list in it and print out this new list.

Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)
print(b)

"""
You will find a one-line code solution below.
"""

c = [i for i in a if i < 5]
print(c)

"""
Another solution by means of user_input as a reference. 
"""

user_input = int(input('Enter a number: '))

d = [i for i in a if i < user_input]
print(d)