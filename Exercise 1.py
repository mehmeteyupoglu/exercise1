#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 1 

Create a program that asks the user to enter their name and their age. Print 
out a message addressed to them that tells them the year that they will turn 
100 years old.

Extras:

    Add on to the previous program by asking the user for another number and 
    printing out that many copies of the previous message. (Hint: order of 
    operations exists in Python) Print out that many copies of the previous 
    message on separate lines. (Hint: the string "\n is the same as pressing 
    the ENTER button)

"""

name = input('Enter your name: ')
user_input = int(input('Enter your age:  '))
the_frequency = int(input('How many times do you want the print function to \
work: '))
current_year = 2019
date_of_birth = current_year - user_input
target_year = date_of_birth + 100

output = 'Dear {}, you will turn 100 in {}. '.format(name.title(), 
               target_year)
for i in range(1, the_frequency):
    print(output)





