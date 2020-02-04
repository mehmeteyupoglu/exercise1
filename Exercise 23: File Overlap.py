#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 24

Given two .txt files that have lists of numbers in them, find the numbers that 
are overlapping. One .txt file has a list of all prime numbers under 1000, and 
the other .txt file has a list of happy numbers up to 1000.

"""
primelist = []

with open('primenumbers.txt') as prime:
    line = prime.readline()
    
    while line:
        
        primelist.append(int(line))
        line = prime.readline()

print(primelist)

happylist = []

with open('happynumbers.txt') as happy:
    line = happy.readline()
    
    while line:
        
        happylist.append(int(line))
        line = happy.readline()

print(happylist)

overlap = [i for i in primelist if i in happylist]
print(overlap)

print(len(overlap))


        
        
        

    


    






