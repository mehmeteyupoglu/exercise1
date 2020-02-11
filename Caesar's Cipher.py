#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:25:41 2020

@author: Mehmet Eyüpoğlu
"""
'''
Caesar's Cipher
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text = 'hello'
output = ''

def shift_amount(i):
    
    '''It helps the text turn back to the beginning of alphabet when the amount
    of shift exceeds the length of alphabet
    '''
    return i % 26

def encrypt(text, required_shift):
    
    text = text.lower()
    output = ''
    
    for i in text:
        if i not in alphabet:
            output = output + i 
        else:
            alpha_index = alphabet.find(i)
            output = output + alphabet[shift_amount(alpha_index+required_shift)]
    
    return output 

text2 = "Let's test the Caesar's Cipher whether it works"

print(encrypt(input_text, 8))
print(encrypt(text2, 7))