#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: Mehmet Eyüpoğlu
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''
#user_input = int(input('Enter a number between 1 and 5:  '))
#
#if user_input == 1:
#    print('one')
#elif user_input == 2:
#    print('two')
#elif user_input == 3:
#    print('three')
#elif user_input == 4:
#    print('four')
#elif user_input == 5:
#    print('five')
#else:
#    print('Invalid input')


'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
#user_input = input('Enter a number between one and five:  ')
#user_input = user_input.lower()
#
#if user_input == 'one':
#    print(1)
#elif user_input == 'two':
#    print(2)
#elif user_input == 'three':
#    print(3)
#elif user_input == 'four':
#    print(4)
#elif user_input == 'five':
#    print(5)
#else:
#    print('Invalid input')


'''
Question 3

Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
#import random
#
#num = random.randint(1,11)
#user_input = 0
#
#
#while user_input != 'exit' or user_input != num:
#    
#    user_input = input('Enter a number between 1 and 10')
#    user_input = user_input.lower()
#    
#    if user_input == 'exit':
#        break 
#    
#    user_input = int(user_input)
#    
#    if user_input > num:
#        print('You are high')
#    elif user_input < num:
#        print('You are low')
#    else:
#        print('Congratulations. You won')


'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
#name = input('Enter your name:  ')
#length = len(name)
#
#if len(name) > 5:
#    print('The length of your name is : {} '.format(length))
#else:
#    print('The length of your name is a secret. ')


'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''

#def two_nums():
#    
#    a = int(input('Enter a number: ==> '))
#    b = int(input('Enter another number: ==>'))
#    
#    if a > 15 and b > 15:
#        return a * b
#    
#    elif a > 15 or b > 15:
#        return a + b
#    
#    elif a < 15 and b < 15:
#        return 0
#    
#math = two_nums()
#print(math)
#    
    

'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
var_1 = int(input('Enter a number: ==>'))
var_2 = int(input('Enter another number: ==>'))

var_1, var_2 = var_2, var_1
print(var_1, var_2)
