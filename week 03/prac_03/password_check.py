"""
CP1404 - Practical
Get a password with minimum length and display asterisks.
"""
MINIMUM_LENGTH = 9


def main():
    """Get user password and print in as aterisks."""
    password = get_password(MINIMUM_LENGTH)
    print('*' * len(password))


def get_password(minimum_length):
    """Get user password."""
    password = input(f"Please enter your password of minimum length {minimum_length}: ")
    while len(password) < minimum_length:
        print("Your Entered Password is too short")
        password = input("Please enter your password ")
    return password


main()
