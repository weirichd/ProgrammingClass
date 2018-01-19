# Number guessing game
#
# By: Dr. David E. Weirich
#
# A player tries to guess a number that the computer is thining of.
# The computer will tell you if your guess is too low, or too high.
# If you can guess in 15 guesses, you win!

# Import this for randint function
import random

number_of_guesses = 0

# STEP 1: Think of a number

number = random.randint(1, 100)

# STEP 2: The player makes a guess

guess = int(input("Please guess a number bewteen 1 - 100: "))

# STEP 3: If the guess is too high, the computer says so,
# If the guess is too low, the computer says so
# If the guess is correct, the player wins!
# If the number of guesses is 15, the player loses!
# Otherwise, the player guesses again. (Go back to step 2)

while guess != number and number_of_guesses < 15:
    number_of_guesses = number_of_guesses + 1
    
    # The guess was higher than the
    if number < guess:
        print("The guess is too high!")
    
    if number > guess:
        print("The guess is too low!")
    
    print('You have used {} guesses.'.format(number_of_guesses))
    guess = int(input("Please guess another number bewteen 1 - 100: "))


if number_of_guesses < 15:
    print("You are a winner!")
else:
    print("You lost. I was thinking of {}".format(number))