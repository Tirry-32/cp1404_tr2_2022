from person import *
# define one object
p = Person("Joanne",20)
print("my name is ", p.name)
print("my age is ", p.age)
print(f"{p.name} {p.age}")
print(p)

#object 2
p2 = Person("Tirivashe",21)
print("my name is ", p2.name)
print("my age is ", p2.age)

list_of_3_people = [Person("Sarah"),Person("Phuc",20),Person("Tiri",21)]
for person in list_of_3_people:
    print(person)
print(p.my_num)
print(p2.my_num)
print(Person.my_num)