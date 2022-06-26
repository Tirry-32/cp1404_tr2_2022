"""
CP1404 - Practical
List Exercises
"""

numbers_list = []
for i in range(1, 6):
    number = int(input("Number : "))
    numbers_list.append(number)

print(f"The first number is {numbers_list[0]} ")
print(f"The last number is {numbers_list[-1]}")
print(f"The smallest number is {min(numbers_list)}")
print(f"The largest number is {max(numbers_list)}")
print(f"The average of the numbers is {sum(numbers_list)/len(numbers_list)} ")

usernames = {'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'}

username = input("Enter you username : ")
if username in usernames:
    print("Access granted")
else:
    print("Access Denied ")
