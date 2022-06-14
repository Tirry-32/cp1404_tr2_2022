# get user input
age = int(input("Enter Age between 0 and 150:"))
while age > 150 or age < 0:
    print("Invalid age")
    age = int(input("Enter Age between 0 and 150:"))

print("Your age:", age)
