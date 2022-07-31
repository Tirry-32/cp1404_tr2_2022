"""
CP1404 Practical
UnreliableCar class, derived from Car
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:  # set distance = 0 when unreliable otherwise proceed
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
