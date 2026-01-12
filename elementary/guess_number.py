"""
Generates a number and prompts the user to guess said number.
"""

import random

answer = random.randint(1, 100)
print("I've generated a super secret number from 1 to a 100. Guess what it is buddy ol' pal.")

not_guessed = True
prev_guess = 0 # Set to zero, as this will never trigger same guess prompt on first guess
num_guesses = 0
while not_guessed:
    guess = int(input(f"Guess {num_guesses+1}: "))
    if guess < 1 or guess > 100:
        print("That's not even within range dude. Try again.")
    elif guess == prev_guess:
        print("That's the same guess. Come on gimme a different one.")
    elif guess < answer:
        num_guesses += 1
        print("Too low.")
    elif guess > answer:
        num_guesses += 1
        print("Too high.")
    elif guess == answer:
        num_guesses += 1
        print(f"{answer} is correct my friend. And it only took you {num_guesses} guesses.")
        not_guessed = False
    prev_guess = guess
