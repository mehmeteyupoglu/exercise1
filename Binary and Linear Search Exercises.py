#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:25:41 2020

@author: Mehmet Eyüpoğlu
"""
'''
Search Exercises
'''

def linear_search(item, my_list):
    '''This function searches through the list in a linear movement'''
    
    i = 0
    found = False
    
    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i += 1
    return found 

a = [1,6,4,0,23,67,45,89,4,3,7]

print(linear_search(23, a))
print(linear_search(34, a))



def binary_search(item, my_list):
    '''It gives the item searched by dividing the list in two in each attempt'''
    
    found = False
    first = 0
    last = len(my_list)
    
    while first <= last and found == False:
        midpoint = (first+last) // 2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found 

print(binary_search(23, a))
print(binary_search(34, a))
            

                    
