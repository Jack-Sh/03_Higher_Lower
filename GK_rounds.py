rounds = 3

rounds_played = 0

while rounds != rounds_played:

    print("Round {}".format(rounds_played + 1))
    rounds_played += 1

    again = input("Again? ")

    if again != "":
        break
