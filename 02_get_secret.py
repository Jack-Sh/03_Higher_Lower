# HL component 2 - get secret

# To Do
# Generate secret number between the given high and low numbers

import random

# For testing purposes lowest equals 1
# and highest equals 10
lowest = 1
highest = 10

# Generate 20 numbers between lowest and highest
for item in range(0, 20):
    secret = random.randint(lowest, highest)
    print(secret, end="\t")