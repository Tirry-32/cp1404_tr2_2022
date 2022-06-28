import operator

name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
name = input("Enter name: ")
age = int(input("Enter age :"))
name_to_age[name] = age
sorted_name_to_age = dict(sorted(name_to_age.items(),key=operator.itemgetter(1),reverse=True))
for key, value in sorted_name_to_age.items():
    print(f"{key:10s}-{value:10d}")