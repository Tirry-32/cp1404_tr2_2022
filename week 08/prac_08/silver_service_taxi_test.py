"""
CP1404 - Practical
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi_1 = SilverServiceTaxi("Test Fancy Taxi", 100, 5)
    taxi_1.drive(18)
    print(taxi_1)
    print(taxi_1.get_fare())


main()
