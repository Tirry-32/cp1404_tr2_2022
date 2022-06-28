names = ['Cue Nguyen', 'Hellene Clinton', 'Sarah Edison']

ages = [50, 30, 20]

#

name_to_age = {'Cue Nguyen': 50, 'Hellene Clinton': 30, 'Sarah Edison': 20}

for key, value in name_to_age.items():
    print(key, value)

for key in name_to_age.keys():
    print(key)

for value in name_to_age.values():
    print(value)
name_to_age['Tony William'] = 34
print(name_to_age)

for key in name_to_age:
    print(name_to_age[key])
# not this way : name_to_age_ = name_to_age

name_to_age_1 = name_to_age.copy()

# produce another dictionary from name_to_age with age < 25
name_to_age_2 = {}
for name, age in name_to_age.items():
    if age < 25:
        name_to_age_2[name] = age

print(name_to_age_2)

# dictionary comprehension
name_to_age_3 = {name:age for name , age in name_to_age.items() if age < 25 }
print(name_to_age_3)