#Functions


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
    print("You will first be asked to choose a number of rounds (this has to be greater than 0)\n
    "You will then have to choose a low number and a high number (greater than 0 up to 500)\n
    "The computer will generate a random number between your two chosen numbers\n
    "The computer will caculate how many guesses are allowed based on your choices\n
    "Then you will have to guess the secret number")
    print()
    print("Have Fun!")



# Main routine


# Valid lists
yes_no_list = ["yes", "no"]

# Ask user if they have played before
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# if played_before equals no show instructions
if played_before_response == "no":
    print(instructions)                                       