# You can also import specific items:
from geometry.shapes import circle_area, Triangle
from geometry.calculations import hypotenuse as h

print(f"\nUsing imported functions directly:")
print(f"Area of circle (direct): {circle_area(7)}")
my_other_triangle = Triangle(5, 12)
print(f"Area of other triangle (direct): {my_other_triangle.area()}")
print(f"Hypotenuse (alias h): {h(6, 8)}")