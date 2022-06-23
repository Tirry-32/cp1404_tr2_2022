def average_value(numbers: list):
    try:
        return sum(numbers)/len(numbers)
    except ZeroDivisionError:
        print('Division Error')
        return None

print(average_value([1, 2, 3]))
print(average_value([]))
for year in range(1900, 2023, 4) :
    print(year)

