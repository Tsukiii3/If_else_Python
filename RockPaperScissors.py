# Rock-Paper-Scissors Game

import random

choices = ['Paper', 'Rock', 'Scissors']
pc = random.randint(0, 2)  # Computer's choice

print('=-' * 20)
player = int(input('ROCK-PAPER-SCISSORS! Choose Paper [0], Rock [1], or Scissors [2]: '))
print('The COMPUTER played {}'.format(choices[pc]))
print('YOU played {}'.format(choices[player]))
print('=-' * 20)

if pc == 0:  # Computer played Paper
    if player == 0:
        print('TIE!')
    elif player == 1:
        print('YOU LOSE!')
    elif player == 2:
        print('YOU WIN!')
    else:
        print('Invalid move!')

elif pc == 1:  # Computer played Rock
    if player == 0:
        print('YOU WIN!')
    elif player == 1:
        print('TIE!')
    elif player == 2:
        print('YOU LOSE!')
    else:
        print('Invalid move!')

elif pc == 2:  # Computer played Scissors
    if player == 0:
        print('YOU LOSE!')
    elif player == 1:
        print('YOU WIN!')
    elif player == 2:
        print('TIE!')
    else:
        print('Invalid move!')