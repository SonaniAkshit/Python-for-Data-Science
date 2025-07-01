# geometry/calculations.py

def hypotenuse(side_a, side_b):
    """Calculates the hypotenuse of a right-angled triangle."""
    return (side_a**2 + side_b**2)**0.5

def get_distance(p1, p2):
    """Calculates the Euclidean distance between two points (tuples)."""
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5