from student import *

# define a student object
one_student = Student("Tom", 22, "jc786539")
print(one_student)

list_of_3_students = [Student("Sarah", 22, "jc786598"), Student("Phuc", 20, "jc765249"),
                      Student("Tiri", 21, "jc781027")]
for student in list_of_3_students:
    print(student)