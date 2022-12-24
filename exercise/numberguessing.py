#number guessing game

import random
winning_number=random.randint(1,100)
guess=1
number=int(input("guess a number between 1 to 100: "))
#game_over=False

while True: #not game_over
    if number==winning_number:
        print(f'you win and you guessed it in {guess} times')
        break
        #game_over=True
    else:
        if number<winning_number:
            print('too low')
            
        else:
            print('too high')   
            
    guess+=1
    number=int(input('guess again: '))
    #or continue
    #DRY principle of coding --> don't repeat yourself
