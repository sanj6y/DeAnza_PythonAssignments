'''
Sanjay Chandrasekar
CIS 41A   Spring 2021
Unit E take-home assignment
Second Script
'''

# Guessing Game

import random

secretNum = random.randint(1,100)

print("Welcome to the guessing game.")
print("You need to guess a number from 1 to 100.")

count = 1

while True:
    guess = int(input("What is your guess? "))
    if guess < secretNum:
        print("Guess is too low.")
    elif guess > secretNum:
        print("Guess is too high.")
    else:
        print("Congratulations!")
        print("You guessed the secret number in " + str(count) + " guesses!")
        break
    count += 1

'''
Execution Results:
Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 45
Guess is too high.
What is your guess? 23
Guess is too low.
What is your guess? 34
Guess is too high.
What is your guess? 27
Guess is too high.
What is your guess? 26
Guess is too high.
What is your guess? 25
Guess is too high.
What is your guess? 24
Congratulations!
You guessed the secret number in 7 guesses!
'''