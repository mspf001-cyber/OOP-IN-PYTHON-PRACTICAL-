"""Practical 11: Dictionary with cubes"""

cube_dict = {x: x**3 for x in range(1, 6)}

print("Dictionary with cubes:")
for key, value in cube_dict.items():
    print(f"{key}: {value}")