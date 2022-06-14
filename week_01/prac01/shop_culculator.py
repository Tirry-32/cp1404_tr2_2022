"""
CP1404 - Practical
Program to determine total price and discount for a shop calculator .
"""
items = int(input("Number of items: "))
total = 0
for i in range(items):
    price_of_item = float(input("Price of item: "))
    total += price_of_item

if total > 100:
    total = total * 0.9  # calculate and include the discount on total

print(f"Total price for {items} items is {total}")
