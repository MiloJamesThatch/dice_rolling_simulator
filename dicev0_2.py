import random
import sys
import os

# Dice Rolling Simulator v.2

print("Welcome to the Dice Rolling Simulator v.2")
print("")
print("Would you like to roll the dice?")
qtn = input("Would you like to roll the dice? ")

if qtn in ['y', 'Y', 'yes', 'Yes', 'YES']:
    dice = random.sample([1, 2, 3, 4, 5, 6], 1)
    print(dice)
else:
    sys.exit()
