#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to 
guess the number, then tell them whether they guessed too low, too high, or 
exactly right. (Hint: remember to use the user input lessons from the very 
first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

from random import randint
num = randint(1, 9)
guess = 0
count = 0

while num != guess or guess != 'exit':
    guess = input('Guess the number between 1 and 9. Enter "exit" to quit:  ')
    guess = guess.lower()
    
    if guess == 'exit':
        break 
    
    guess = int(guess)
    count += 1
    
    if guess < num:
        print('You are low')
    elif guess > num:
        print('You are high')
    else:
        print('Congratulations. You found the number.')
        print('It took you {} times to find {}. '.format(count, num))





