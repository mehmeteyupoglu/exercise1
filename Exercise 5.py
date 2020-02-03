#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Take two lists and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). Make sure your 
program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at 
this point - we’ll get to it soon)

"""

a = [1, 1, 2, 3, 5, 8, 13, 11, 11, 21, 34, 55, 55, 55, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 55, 55, 12, 13]
c = []

for i in a:
    if i in b:
        if i not in c:
            c.append(i)

print(c)

"""
In one line of code: 
"""

d = [i for i in set(a) if i in set(b)]

print(d)


import random 
list1 = list(range(1,random.randint(1, 15), 3))
list2 = list(range(1,random.randint(1, 29), 2))

e = [i for i in set(list1) if i in set(list2)]

print(e)




