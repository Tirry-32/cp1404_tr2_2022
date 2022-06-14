valid_input = False
while not valid_input:
    try:
        age = int(input('Age: '))
        if age < 0 or age > 150 :
            print('Age must be between 0 and 150. ')
        else:
            valid_input = True
    except ValueError:
        print('Invalid (not an integer )')
if age % 2:
    print(f'{age} is odd')
else:
    print(f'{age} is even')