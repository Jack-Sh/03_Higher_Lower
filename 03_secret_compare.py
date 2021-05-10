# HL component 3 - compare secret and users guess

# To Do
# If users guess is below secret print too low
# If users guess is above secret print too high
# If users guess is the secret print congratulations


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


lowest = 1
highest = 10
SECRET = 5

guess = ""

while guess != SECRET:

    guess = int_check("Guess: ", lowest, highest)

    if guess < SECRET:
        print("Too low! Try again")
    elif guess > SECRET:
        print("Too high! Try again")
    else:
        print("Congratulations! You guessed the secret number")
