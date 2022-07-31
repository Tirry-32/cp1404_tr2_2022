"""
CP1404 Practical
"""

from unreliable_car import UnreliableCar


def main():
    """Test Car  reliability."""

    good_car = UnreliableCar("Mostly Good", 100, 90)  # Good working car
    bad_car = UnreliableCar("Usually unreliable", 100, 9)  # bad car

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 20, 3):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


main()
