# Make a Project of guessing number.

import random

# Randomly select a number between 1 and 100
number_to_guess = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 3

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

# Loop until the player guesses the correct number
while guess != number_to_guess and attempts < max_attempts:
    try:
        # Take user input
        # print(number_to_guess)

        guess = int(input("Enter your guess: "))
        attempts += 1

        # Provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid integer.")
    
if guess != number_to_guess:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

print("Thanks for playing the Number Guessing Game!")
