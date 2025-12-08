"""Practical 10: Point class with distance calculation"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Demo
p1 = Point(3, 4)
p2 = Point(6, 8)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {p1.distance(p2):.2f}")