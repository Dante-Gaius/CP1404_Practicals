from cp1404practicals.Prac_06.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, car_name, fuel, reliability):
        super().__init__(car_name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 101)
        if random_number >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven
