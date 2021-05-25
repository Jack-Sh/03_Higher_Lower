import random
import math

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
    print()


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


# Main routine
SECRET = ""

already_guessed = []
game_summary = []

rounds_played = 0
rounds_won = 0
rounds_lost = 0

max_guesses = ""
guesses_left = max_guesses

guess = ""

end_game = "no"

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

# Check all given numbers
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1, 1000, "")

for item in range(0, 4):

    num_range = highest - lowest + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

# Start of game loop
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
            rounds_played -= 1
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

    # if the guess is not 'xxx' then add the outcome to the list
    if guess != "xxx":

        # outcome format
        if result == "lost" or result == "won":
            outcome = "Round {}: you {}".format(rounds_played, result)

        # structures outcome in a list
        game_summary.append(outcome)

# Ask user if they want to see their game history
game_score = "Do you want to see your game history? "
game_score_response = choice_checker(question=game_score, valid_list=yes_no_list, error="Please enter yes or no")

# If 'yes' show game history in list format
if game_score_response == "yes":
    print()
    print("Game History")
    for game in game_summary:
        print(game)

# Calculate game stats in percentages
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

# Show game statistics in percentages and number of W / L
print()
print("Game Statistics")
print("Win: {}, ({:.0f}%)\nLoss {}, ({:.0f}%)"
      .format(rounds_won, percent_win, rounds_lost, percent_lose,))
print()

# print end game message
print("Thanks for Playing!")
