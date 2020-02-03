#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""
"""
Exercise 8

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors,
Scissors beats paper,
Paper beats rock.

"""
user_input1 = input('Choos one: rock, paper, scissors? ')
user_input2 = input('Choos one: rock, paper, scissors? ')
user_input1 = user_input1.lower()
user_input2 = user_input2.lower()

def compare(u1, u2):
    
    if u1 == u2:
        print('It is a tie.')
    
    elif u1 == 'rock':
        if u2 == 'scissors':
            print('Rock wins')
        else:
            print('Paper wins')
    elif u1 == 'paper':
        if u2 == 'rock':
            print('Paper wins')
        else:
            print('Scissors win')
    
    elif u1 == 'scissors':
        if u2 == 'rock':
            print('Rock wins')
        else:
            print('Scissors win')
    
    else:
        print('Invalid input')
    
compare(user_input1, user_input2)
    
