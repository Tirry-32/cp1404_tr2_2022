"""
CP1404 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    elif 50 > score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()
