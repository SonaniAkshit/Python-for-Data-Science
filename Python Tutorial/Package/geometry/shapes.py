# geometry/shapes.py

def circle_area(radius):
    """Calculates the area of a circle."""
    return 3.14159 * radius * radius

def square_perimeter(side):
    """Calculates the perimeter of a square."""
    return 4 * side

class Triangle:
    """A simple Triangle class."""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height