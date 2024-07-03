import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

player_move = input('Choose [r]ock, [p]aper, or [s]cissors:')

if player_move == 'r':
    player_move = rock
    print("player chose rock") 
elif player_move == 'p':
    player_move = paper 
    print("player chose paper") 
elif player_move == 's':
    player_move = scissors
    print("player chose scissors") 
else:
    print('Invalid Input. Try again....')
    
computer_random_number = random.randint(1,3)
computer_move = ''

if computer_random_number == 1:
    computer_move = rock
    print('computer chose rock')
elif computer_random_number == 2:
    computer_move = paper
    print('computer chose paper')
else:
    computer_move = scissors
    print('computer chose scissors')

if player_move == computer_move:
     print('Draw!')
elif (player_move == rock and computer_move == scissors) or \
     (player_move == paper and computer_move == rock) or \
     (player_move == scissors and computer_move == paper):
     print('You Win!')
else:
    print('You Lose!')
    
