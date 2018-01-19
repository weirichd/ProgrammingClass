# Number guessing game 2
#
# By David Weirich

import random

print("Welcome to the number game!")
print("Please think of a number between 1 and 100.")
print("I will try to guess it.")

# Store lowest and highest guess so far
low = 1
high = 100

# Store the number of guesses
number_of_guesses = 0

# 1 means too low, 2 means too high, 3 means it won
instruction = ''

while instruction != '3' and number_of_guesses < 15:
    # Mave the computer make a guess
    guess = random.randint(low, high)
    
    # Increase the number of guesses
    number_of_guesses = number_of_guesses + 1
    
    # Tell us the guess
    print("My guess is {}.".format(guess))
    
    # Ask if the guess is correct
    instruction = input('How was my guess? (1 - too low, 2 - too high, 3 - I won ')
    
    # Update low and high to narrow the possible guesses
    if instruction == '1':
        low = guess + 1
        
    if instruction == '2':
        high = guess - 1

if number_of_guesses == 15:
    print("Ok. I used 15 guesses and still didn't get it. I give up :(")
    
print('Thanks for playing!')