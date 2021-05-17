import random

# Functions


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


# Functions to display instructions when called
def instructions():
    print()
    print("How to play!")
    print()
    print("For each game you will be asked to...")
    print("- Enter a 'low' and a 'high' number.")
    print("- The computer will then generate the secret number")
    print("- The computer will caculate how many guesses you get")
    print("- Enter the number of rounds you want to play")
    print("- Begin guessing the secret number")
    print()
    print("Good Luck!")


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
GUESSES_ALLOWED = 5

rounds_played = 0

guesses_left = GUESSES_ALLOWED

guess = ""

# Check all given numbers
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

# Valid lists
yes_no_list = ["yes", "no"]

# Ask user if they have played before
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# if played_before is equal to 'no' show instructions
if played_before_response == "no":
    instructions()
