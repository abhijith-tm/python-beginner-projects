import random
move_number = random.randrange(0, 2)
computer_move = ['rock', 'paper', 'scissor']

while True:
    user_move = input('Enter rock, paper, scissor or quit to quit: \n')
    print('Computer chose ', computer_move[move_number])
    if computer_move[move_number] == user_move:
        continue
    elif user_move == 'rock' and computer_move[1]:
        print('computer won')
    elif user_move == 'rock' and computer_move[2]:
        print('user won ')
    elif user_move == 'paper' and computer_move[0]:
        print('User won')
    elif user_move == 'paper' and computer_move[2]:
        print('user won')
    elif user_move == 'scissor' and computer_move[0]:
        print('Computer won')
    elif user_move == 'scissor' and computer_move[1]:
        print('user won')
    elif user_move == 'quit':
        exit()