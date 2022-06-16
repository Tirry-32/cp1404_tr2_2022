
"""
CP1404 - Practical
Broken program to determine score status
"""



score = float(input("Enter score: "))
if 90 <= score <= 100:
    print("Excellent")
elif 90 > score >= 50:
    print("Passable")
elif 50 > score >= 0:
    print("Bad")
else:
    print("Invalid score")
