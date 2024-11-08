
# Make a program that simulates a guessing game where the computer chooses a random number between 1 and 100, and the user has to guess it.

import random

target_number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break

