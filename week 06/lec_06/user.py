class User(object):
    # constructor
    def __init__(self, name="unknown", num_of_tacos=5, score=0):
        #  instance variables
        self.name = name
        self.num_of_tacos = num_of_tacos
        self.score = score

    # give a taco to another user
    def give_a_taco_(self, another_user):
        if self.num_of_tacos > 0:
            self.num_of_tacos -= 1
            another_user.num_of_tacos += 1
            self.score += 1
        else:
            print("Sorry no tacos left to give away.")

    def __str__(self):
        return f"{self.name} , {self.score} points , {self.num_of_tacos} tacos left"
