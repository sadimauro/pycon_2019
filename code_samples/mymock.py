#!/usr/bin/env python3

from unittest.mock import MagicMock
import dataclasses
import random


@dataclasses.dataclass
class Engine:
    model: str
    horsepower: int
    pistons: int


@dataclasses.dataclass
class Tire:
    make: str
    model: str
    diameter: float
    psi: int


@dataclasses.dataclass
class Car:
    make: str
    model: str
    tires: list
    tires_no: int
    engine: Engine

    def drive(self, speed=80):
        return f"vroom...you're flying down the road at {speed} mph"

    def get_value(self):
        # pretend there's some complicated formula here
        return 20000 + random.randint(-18000, 18000)

    def get_top_speed(self):
        # let's assume that the top speed of the car is a function of the car's value
        return 60 + int(self.get_value() / 3000)


if __name__ == "__main__":
    engine = Engine("Hemi", 220, 6)
    tire = Tire("Goodyear", "Greattire", 21.3, 35)
    car = Car("Honda", "Accord", [tire, tire, tire, tire], 4, engine)

    # instead of calling the actual car.get_value(), since (we're pretending) it's variable, resource-intensive, or the like, we mock it.
    car.get_value = MagicMock(return_value=30000)

    try:
        assert car.get_top_speed() == 70
        print("assert passed.")
    except AssertionError:
        print("assert failed!")
