#This is a guess game ,the program will take a random number from 0 to 9
#we have to guess it correctly



import random
random_number = random.randrange(1, 10)

while True:
    guess_number = input( " guess a number " )
    guess_number = int(guess_number)
    guess = 1
    guess += 1
    if random_number == guess_number:
        print('You got it')
        break
    elif random_number < guess_number:
        print("you are above the number")
    else:
        print('You are below the number')
print("it took you ", guess, "guess to find the number" )
