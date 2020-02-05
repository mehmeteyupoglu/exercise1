# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: Mehmet Eyüpoğlu
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }

#user_input = input('Which capital would you like to see ? ')
#user_input = user_input.title()
#
#while user_input != 'exit' or not user_input.isalpha():
#    
#    user_input = input('The input must be a country. Please enter a country:  ') 
#    
#    if user_input == 'exit':
#        print('Exiting...')
#        break
#    
#
#    if capitals[user_input] in capitals:
#        print(capitals[user_input])
#        
#    elif user_input == 'United States':
#        print('Washington DC')
#        
#    elif user_input == 'United Kingdom':
#        print('London')
#        
#    else:
#        print('Our dictionary does not contain the information you entered. ')

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
#a, b = 0, 1
#fib = []
#dic = {}
#
#for i in range(0, 13):
#    a, b = b, a+b
#    dic[i] = a
#
#print(dic)


'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#key_names = ['Open','High','Low','Close']
#prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
#d_1 = {}
#
#for i in range(len(key_names)):
#    d_1[companies[i]] = dict(zip(key_names, prices[i]))
#
#print(d_1)

 

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
#import datetime
#
#now = datetime.date.today()
#holiday = datetime.date(2020, 7, 5)
#delta = holiday - now
#
#print('There are {} days until the holiday!'.format(delta.days))



'''
Question 5
Create a dictionary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
#import random
#keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#d = {}
#
#for i in keys:
#    d[i] = random.randint(1, 100)
#    
#print(d)
#
#from matplotlib import pyplot as plt
#
#x, y = zip(*d.items())
#
#print(plt.bar(x,y))
