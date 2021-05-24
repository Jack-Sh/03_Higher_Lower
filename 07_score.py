# HL component 7 - implement score mechanics

# To Do
# add outcome variable
# ask user if they want to see their score (outcome)

import random


# Function to check low, high, guess, and round numbers
def int_check(question, low=None, high=None, exit_code=None):

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

        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

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


# Choice checker function, response must be out of a specified valid list
# also works for the first letter of the word
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        else:
            print(error)


# Main routine

SECRET = ""

already_guessed = []
game_summary = []

rounds_played = 0

GUESSES_ALLOWED = 5
guesses_left = GUESSES_ALLOWED

guess = ""

# Valid lists
yes_no_list = ["yes", "no"]

# Check all given numbers
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1, 1000, "")
# Start of game loop

end_game = "no"
# if the user hasn't played all the given rounds
# continue the loop
while rounds_played != rounds:

    if end_game == "yes":
        break

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
        guess = int_check("Guess: ", lowest, highest, "xxx")
        if guess == "xxx":
            end_game = "yes"
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
            result = "won"

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
            result = "lost"

        # if user runs of of guesses or guesses secret and hasn't played all given rounds
        # continue the loop, reset the list of guesses and reset guesses allowed
        if guess == SECRET or guesses_left == 0 and rounds_played != rounds:
            GUESSES_ALLOWED = 0
            GUESSES_ALLOWED += 5
            guesses_left = GUESSES_ALLOWED
            already_guessed.clear()
            break

if result == "lost" or result == "won":
    outcome = "Round {}: you {}".format(rounds_played + 1, result)

game_summary.append(outcome)

# Ask user if they want to see their game score
game_score = "Do you want to see your game history? "
game_score_response = choice_checker(question=game_score, valid_list=yes_no_list, error="Please enter yes or no")

# If 'yes' show game score
if game_score_response == "yes":
    print()
    print("Game History")
    for game in game_summary:
        print(game)

# print end game message
print("Thanks for Playing!")
