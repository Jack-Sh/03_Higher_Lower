# HL component 2 - get secret

# To Do
# Generate secret number between the given high and low numbers

import random

lowest = 1
highest = 10

for item in range(0, 20):
    secret = random.randint(lowest, highest)
    print(secret, end="\t")