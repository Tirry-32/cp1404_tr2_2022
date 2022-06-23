"""
CP1404 Practical
Quick pick program
"""

import random


NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate random numbers and displays them in one line."""
    number_of_quick_picks = int(input("Number of quick picks : "))
    while number_of_quick_picks < 0:
        print("Invalid Output")
        number_of_quick_picks = int(input("NUmber of quick picks : "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_IN_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:3}" for number in quick_pick))


main()
