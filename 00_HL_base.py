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


# Main routine


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
