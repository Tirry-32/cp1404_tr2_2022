"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When the input is a non integer value
2. When will a ZeroDivisionError occur?
   When the denominator is zero .
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes with the use of a while loop
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator use a number that's not zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")