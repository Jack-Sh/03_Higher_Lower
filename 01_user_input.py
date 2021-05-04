# HL component 1 - Get and check user input

# To Do
# Check a lowest is an intger (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest
# (lower and upper bound)

# Number checking funtion
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

SECRET = 5

GUESSES_ALLOWED = 5

rounds_played = 0

guesses_left = GUESSES_ALLOWED

guess = ""

# Check all given numbers
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

# Beginning of game loop
# Whilst the secret number isn't guessed
# and the user hasn't run out of guesses
# continue the loop
while guess != SECRET and guesses_left >= 1:

    # Print rounds heading based on rounds chosen
    if rounds != "":
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)
        print(heading)

    # Ask user for guess and check that it's valid
    guess = int_check("Guess: ", lowest, highest)
    
    # Take one away from guesses left everytime a number is guessed
    guesses_left -= 1

    # If user guesses secret congratulate go next round
    if guess == SECRET:
        print("Congratulations you guessed the secret number")
        rounds_played += 1

    # If the user has run out of guesses go next round
    elif guesses_left < 1:
        print("You have run out of guesses")
        rounds_played += 1

    # If the user has played all rounds chosen
    # break the loop
    if rounds_played != rounds:
        continue
    else:
        break
