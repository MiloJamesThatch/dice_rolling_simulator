import random
import sys
import os

# Dice Rolling Simulator v.3

print("Welcome to the Dice Rolling Simulator v.3")

print("")

qtn = input("Would you like to roll the dice? ")

print("")

if qtn in ['y', 'Y', 'yes', 'Yes', 'YES']:
    dice = random.sample([1, 2, 3, 4, 5, 6], 1)
    print('The dye reads', dice)
else:
    print("Alright...program terminating...")
    sys.exit()
