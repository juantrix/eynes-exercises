import math


class Circle():
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative or zero")
        self.radius = radius
