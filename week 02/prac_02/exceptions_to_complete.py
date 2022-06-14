"""
CP1404 - Practical
"""
finished = False
result = 0
while not finished:
    try:
        value = int(input("Please enter an integer value:"))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
