import math


class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius cannot be negative or zero")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius cannot be negative or zero")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("Multiplier cannot be negative or zero")
        return Circle(self.radius * n)
