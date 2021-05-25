# HL component 9 - add in max guesses caculator

import math

for item in range(0, 4):

    low = int(input("Low: "))
    high = int(input("High: "))

    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
