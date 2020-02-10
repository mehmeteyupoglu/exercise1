'''
author: Mehmet Eyüpoğlu
'''

import random
maximum = 100
minimum = 0
number = random.randint(minimum, maximum)
running = True
answer = None
Try = 0

while running:
    
    answer = input('Is it {}\n==>'.format(number))
    
    if 'no' in answer.lower() and 'higher' in answer.lower():
        number += random.randint(1,4)
    elif 'no' in answer.lower() and 'lower' in answer.lower():
        number -= random.randint(1,4)
    
    elif answer.lower() == 'no': 
        answer = input('Higher or lower?\n==>')
        if answer.lower() == 'higher':
            number += random.randint(1,4)
        elif answer.lower() == 'lower':
            number -= random.randint(1,4)
    
    elif answer.lower() == 'yes':
        running = False
        
        if Try < 3:
            print('You win. It took you only {} times.'.format(Try))
        elif Try > 2 and Try < 10:
            print('That is not bad. It took you {} times to find the number.'.format(Try))
        
        else:
            print('It took you {} times. It is really bad for a robot...'.format(Try))
    
    Try += 1
    
print('\nThanks for the game')
    
        
        
    
        
            
        
    
