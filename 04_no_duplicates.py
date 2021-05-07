# HL component 4 - don't allow duplicate guesses

# To Do
# set up empty list called already_guessed
# when user enters a valid guess add it to the list
# for each guess check it's not in already guessed


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

SECRET = 5
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED

lowest = 1
highest = 10

guess = ""

# Start of game loop
while guess != SECRET and guesses_left >= 1:

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
    
    if guesses_left == 0:
        print("You have run out of guesses. Good try!")