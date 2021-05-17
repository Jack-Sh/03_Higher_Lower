# HL component 5 - add in round mechanics

# To Do
# set up round heading
# create a loop based on how many rounds the user chose

import random


# Function to check low, high, guess, and round numbers
def int_check(question, low=None, high=None):

    situation = ""

    # If user has specified a low and a high
    # number (eg. when guessing)
    # set the situation to 'both'
    if low is not None and high is not None:
        situation = "both"

    # If user has only specified a low number
    # (eg. when enetering high number)
    # set situation to 'low only'
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or
            # too low if both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main routine

SECRET = ""

already_guessed = []

rounds_played = 0

GUESSES_ALLOWED = 5
guesses_left = GUESSES_ALLOWED

guess = ""

# Check all given numbers
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

# Start of game loop

while rounds_played != rounds:

    # If user enters a valid integer print heading
    # If user enters <enter> print heading
    if rounds != "":
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        rounds_played += 1

    # Get secret
    SECRET = random.randint(lowest, highest)
    print(SECRET)

    while guess != SECRET and guesses_left != 0:

        guess = int_check("Guess: ", lowest, highest)

        # Checks that guess isn't duplicate
        if guess in already_guessed:
            print("You already guessed than number! Please try again. You still have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low! Try a higher number. You have {} guesses left".format(guesses_left))

            elif guess > SECRET:
                print("Too high! Try a lower number. You have {} guesses left".format(guesses_left))
        else:
            if guess < SECRET:
                print("Too low!")

            elif guess > SECRET:
                print("Too high!")

        if guess == SECRET:

            if guesses_left + 1 == GUESSES_ALLOWED:
                print("Amazing! You guessed the secret number first try!")

            else:
                print("Well done! You guessed the secret number with {} guesses remaining".format(guesses_left))

        if guesses_left == 0 and guess != SECRET:
            print("You have run out of guesses. Good try!")

        if guess == SECRET or guesses_left == 0 and rounds_played != rounds:
            GUESSES_ALLOWED = 0
            GUESSES_ALLOWED += 5
            guesses_left = GUESSES_ALLOWED
            already_guessed.clear()

print("Thanks for Playing!")
