import random
import sys
import os

# Dice Rolling Simulator v.2

print("Welcome to the Dice Rolling Simulator v.2")
print("")
print("Would you like to roll the dice?")
qtn = sys.stdin.readline()

if qtn == "y" or "yes":
    dice = random.sample([1, 2, 3, 4, 5, 6], 1)
    print(dice)
else:
    sys.exit()
