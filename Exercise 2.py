#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 2 

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number 
to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.

"""

user_input = int(input('Enter a number to check:  '))
    
if user_input % 2 == 0 and user_input % 4 == 0:
    print(f'{user_input} is an even number and it also can be divided by 4.')
    
elif user_input % 2 == 0:
    print(f'{user_input} is an even number.')
    
else:
    print(f'{user_input} is an odd number. ')
