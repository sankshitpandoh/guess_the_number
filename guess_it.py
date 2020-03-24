import random
import sys
secret_number = random.randint(1,100)
print('I am thinking of a number between 1 and 100')
guess = 0
tries = 1
while guess != secret_number:
    print('Take a Guess')
    guess = int(input())
    if guess == secret_number:
        print('good job, you guessed the number in' +str(tries)+ 'guesses')
        sys.exit()
    elif guess > secret_number:
        print('your guess is too high')
        tries = tries + 1
    else:
        print('your guess is too low')
        tries = tries + 1
