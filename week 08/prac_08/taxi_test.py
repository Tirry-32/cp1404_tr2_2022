"""
CP1404 Practical
Test taxi
"""
from taxi import Taxi


def main():
    """Test Taxi class."""
    taxi_1 = Taxi("Prius 1", 100)
    taxi_1.drive(40)
    print(taxi_1)
    taxi_1.start_fare()
    taxi_1.drive(100)
    print(taxi_1)


main()
