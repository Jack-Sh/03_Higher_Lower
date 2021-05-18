# HL component 5 v3 - add in 'xxx' exit code

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

        response = input(question)

        if situation == "both" and response == "xxx":
            break
        else:

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


# Checks specifically rounds, if it is infinite or an integer
def check_rounds():

    while True:
        # Ask user how many rounds
        response = input("Rounds: ")

        round_error = "Please enter an integer greater than 0"

        # If user DOESN'T type <enter> check to see
        # if it is a valid integer

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            # If the user doesn't type a valid response
            # print an error message (program won't break)

            except ValueError:
                print(round_error)
                continue

        return response


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
rounds = check_rounds()
# Start of game loop

# if the user hasn't played all the given rounds
# continue the loop
while rounds_played != rounds:

    # If user enters a valid integer print heading
    # If user enters <enter> print heading
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)

    print()
    print(heading)
    print()
    rounds_played += 1

    # Get secret
    SECRET = random.randint(lowest, highest)
    print(SECRET)

    # if the secret is guessed or user runs out of guesses
    # break the loop
    while guess != SECRET and guesses_left != 0:

        # get users guess and check that it's valid
        guess = int_check("Guess: ", lowest, highest)
        if guess == "xxx":
            break

        # checks that guess isn't duplicate
        if guess in already_guessed:
            print("You already guessed than number! Please try again. You still have {} guesses left".format(guesses_left))
            continue

        # add valid guess to list and
        # take away 1 from total guesses
        guesses_left -= 1
        already_guessed.append(guess)

        # if user has more than one guess left print one of the following statements
        if guesses_left >= 1:

            # if user guesses lower than secret
            if guess < SECRET:
                print("Too low! Try a higher number. You have {} guesses left".format(guesses_left))

            # if user guesses higher than secret
            elif guess > SECRET:
                print("Too high! Try a lower number. You have {} guesses left".format(guesses_left))

        # if user has 1 guess left
        else:

            # if user guesses lower than secret
            if guess < SECRET:
                print("Too low!")

            # if user guesses higher than secret
            elif guess > SECRET:
                print("Too high!")

        # if user guesses secret print one of the following statements
        if guess == SECRET:

            # if user guesses secret first try
            if guesses_left + 1 == GUESSES_ALLOWED:
                print("Amazing! You guessed the secret number first try!")

            # if user guesses secret (print guesses left)
            else:
                print("Well done! You guessed the secret number with {} guesses remaining".format(guesses_left))

        # if the user runs out of guesses and doesn't guess the secret
        # print statement
        if guesses_left == 0 and guess != SECRET:
            print()
            print("You have run out of guesses. Good try!")

        # if user runs of of guesses or guesses secret and hasn't played all given rounds
        # continue the loop, reset the list of guesses and reset guesses allowed
        if guess == SECRET or guesses_left == 0 and rounds_played != rounds:
            GUESSES_ALLOWED = 0
            GUESSES_ALLOWED += 5
            guesses_left = GUESSES_ALLOWED
            already_guessed.clear()
            break

# print end game message
print("Thanks for Playing!")
