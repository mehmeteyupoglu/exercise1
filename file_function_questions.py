# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''
#def sum_two(a,b):
#    
#    return a + b
#
#print(sum_two(4,56))

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''
#def multiply(a, b = 2):
#    return a * b
#
#print(multiply(3))


'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''
#def power(a, b = 2):
#    return a ** b
#
#print(power(4))
#
#print(power(3,3))

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''
with open('capitals.txt', 'w') as capitals:
    capitals.write('London, Madrid, Berlin, Dublin, Oslo')


'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''

with open('capitals.txt', 'a') as capitals:
    capitals.write('\nParis, Budapest, Bucharest')

with open('capitals.txt') as capitals:
    f = capitals.read()
    print(f)


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

with open('capitals.txt') as infile:
    x = infile.read()  

with open('outfile.txt', 'w') as outfile:
    y = outfile.write(x)
    
print(y)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    