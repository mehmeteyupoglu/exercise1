#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 12

Write a program that takes a list of numbers (for example, 
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last 
elements of the given list. For practice, write this code inside a function.

"""
#a = [5, 10, 15, 20, 25]
#def list_end(a_list):
#    return a_list[0], a_list[len(a_list)-1]
#
#b = list_end(a)
#print(b)



"""
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate and 
then generates them. Take this opportunity to think about how you can use 
functions. Make sure to ask the user to enter the number of numbers in the 
sequence to generate.

"""

#def generate_fib():
#    u_input = int(input('How many fibonacci numbers would you like to generate?'))
#    
#    a, b = 0, 1
#    fib = []
#    
#    for i in range(1, u_input+1):
#        a, b = b, a+b
#        fib.append(a)
#    return fib
#
#fibonacci = generate_fib()
#print(fibonacci)

"""
Exercise 14

Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a 
list, and another using sets.
"""


#This is the first solution: 

#def list_dup(a_list):
    
#    b = []
#    
#    for i in a_list:
#        if i not in b:
#            b.append(i)
#    return b
#
#a = [1,5,4,8,1,4,6,3,34,8,56,90,23]
#
#c = list_dup(a)
#print(c)

#This is the second solution: 

#def list_dup2(a_list):
#    '''
#    This gives the same result in one line of code.
#    '''
#    b = [i for i in set(a_list)]
#    return b
#
#print(list_dup2(a))

"""
Exercise 15

Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My

shown back to me.

"""



#def rvs_word():
#    
#    user_input = input('Enter a sentence')
#    rvs = ' '.join(user_input.split()[::-1])
#    
#    return rvs
#
#result = rvs_word()
#print(result)

"""
Exercise 16

Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new 
password every time the user asks for a new password. Include your run-time 
code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, 
pick a word or two from a list.

"""

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@\
#$%ˆ&*_+'

def password_gen():
    
    global characters
    
    import random
    
    password = ''.join(random.sample(characters, 8))
    
    return password

c = password_gen()

print(c)
    




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
