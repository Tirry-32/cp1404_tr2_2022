"""

Brief description ...

Name:

Date started:

GitHub URL:

"""



# Constants

FILE_NAME = "places.csv"

MENU = 'Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit'



CITY = 0

COUNTRY = 1

PRIORITY = 2

VISITED_STATUS = 3





def load_places(csv_file, places: list):

    try:

        infile = open(csv_file, 'r')

        for line in infile:

            temp_list = line.strip().split(',')

            places.append(temp_list)

        infile.close()

        print("{} places loaded from {}".format(len(places), FILE_NAME))

    except IOError as error:

        print("I/O error: {}".format(error))





def list_places(places: list):

    print('choice L')





def add_new_place(places: list):

    print('choice A')





def mark_a_place_visited(places: list):

    print('choice M')





def save_places(csv_file, places: list):

    print('{} places saved to {}'.format(len(places), csv_file))





def main():

    print("Travel Tracker 1.0 - by student name")

    places = []

    load_places(FILE_NAME, places)

    print(MENU)

    choice = input(">>> ").strip().upper()

    while choice != 'Q':

        if choice == 'L':

            list_places(places)

        elif choice == 'A':

            add_new_place(places)

        elif choice == 'M':

            mark_a_place_visited(places)

        else:

            print("Invalid menu choice")

        print(MENU)

        choice = input(">>> ").strip().upper()

    save_places(FILE_NAME, places)

    print("Bye.")





if __name__ == '__main__':

    main()