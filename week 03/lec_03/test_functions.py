"""
Testing for functions
"""

def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 1.8 + 32.0


def is_even(number):
    # return number % 2 == 0
    return not number % 2


def square(number):
    """Square the number."""
    return number ** 2


def main():
    # print(f'{celsius_to_fahrenheit(21):,.1f}')
    f_degree = celsius_to_fahrenheit(21)
    # number = int(input('Get number : '))
    print(f'{f_degree:.1f}')
    print(is_even(15))
    number = 5
    print(f'{number} ^ 2 =', square(number))


main()  # Start the program
