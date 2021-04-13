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


rounds_played = 0

guesses = 5

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

# Beginning of game loop
end_game = "no"
while end_game == "no":

    if rounds != "":
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)
        print(heading)

    guess = int_check("Guess: ", lowest, highest)
    guesses = guess - 1

    if guesses == 0:
        print("You have run out of guesses")
