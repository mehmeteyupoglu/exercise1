#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Mehmet Eyüpoğlu
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''

#user_input = int(input('Enter a number between 1 and 100 ==> '))
#user_input2 = int(input('Enter another number between {} and 100 ==> '.format(user_input)))
#liste = []
#
#for i in range(user_input, user_input2+1):
#    liste.append(i)
#
#print(liste)

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

#word = input('Enter a word: ')
#rvs = ''
#
#for i in word:
#    rvs = i + rvs
#
#print(rvs)


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
#num = int(input('Enter a number between 1 and 12:  '))
#
#welcome = f'Welcome to {num} times table!'
#
#print('*' * len(welcome))
#print(welcome)
#print('*' * len(welcome))
#print()
#result = 0
#
#
#for i in range(1, 13):
#    result = i * num
#    print('{} x {} = {}'.format(i, num, result))
#
#print()
#print('#' * len(welcome))


'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
#result = 0
#
#for i in range(1, 13):
#    
#    welcome = f'{i} Times Table'
#    print()
#    print(welcome)
#    print('*' * len(welcome))
#    
#    for x in range(1,13):
#        result = i*x
#        print(f'{i} x {x} = {result}')

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

#user_input = input('Please enter a number: ')
#numbers = []
#result = 0
#
#
#while user_input.lower() != 'exit':
#    while not user_input.isdigit:
#        user_input = input('Please enter a digit: ') 
#    numbers.append(int(user_input))
#    user_input = input('Enter another: ')
#for i in numbers:
#    result += i
#    
#mean = result / len(numbers)
#
#print('The mean of {} is {}'.format(numbers, mean))
    

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
#fact = 1
#facto = []
#
#for i in range(1, 5):
#    fact = fact * i
#    facto.append(fact)
#print(facto)


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
#a, b = 0, 1
#fib = []
#
#for i in range(1, 21):
#    a, b = b, a+b
#    fib.append(a)
#
#print(fib)



'''
Question 8

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
star = '*'

#for i in range(1, 7):
#    for x in range(1,6):
#        if i == 1 and x < 6:
#            print(star, end = '')
#        elif i == 2 and x == 1:
#            print()
#            print(star)
#        elif i ==3 and x < 5:
#            print(star, end = '')
#        elif i == 4 and x == 1:
#            print()
#            print(star)
#        elif i == 5 and x == 1:
#            print(star)
#        elif i == 6 and x == 1:
#            print(star)

'''
Question 9
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

odd = []
even = []

for i in range(1,100):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)




























