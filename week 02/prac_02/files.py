"""
CP1404 - Practical
Quick file opening/writing/reading exercises
"""
# Part 1

out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)

# Part 2

out_file.close()
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# Part 3

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Part 4

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
