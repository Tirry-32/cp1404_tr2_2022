"""
CP1404 - Practical
Loops
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_starts = int(input("Number of stars: "))
for i in range(number_of_starts):
    print('*', end=' ')
print()

for i in range(1, number_of_starts + 1):
    print('*' * i)
print()
