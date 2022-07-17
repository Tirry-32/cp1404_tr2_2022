from person import *


class Student(Person):
    def __init__(self, name="unknown", age=18, id="jc786543"):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return super().__str__() + " " + self.id
