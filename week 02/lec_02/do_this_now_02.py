try:
    infile = open('cp111.csv', 'r')
    # read one line at one time
    for line in infile:
        print(line.strip())
    infile.close()
except FileNotFoundError as err:
    print(f'Error :{err}')
