number_of_people = 0
try :
    age = int(input('Enter age (-1 to quit) : '))
    total_age = 0
    while age > -1:
        number_of_people += 1
        total_age += age
        age = int(input('Enter age (-1 to quit) : '))
    if number_of_people > 0:
        print('Avarage age of {} is {:8.2f}'.format(number_of_people, total_age/number_of_people))
    else:
        print('No valid ages entered ')
except ValueError as error:
    print(f'Error : {error}')
