class Person(object):
    my_num = 20 # define class variable can be shaared among objects
    def __init__(self, name="unknown", age=18):
        self.name = name  # define instance variables  (or attributes)
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"
