"""Practical 03: Create pyramid patterns"""

rows = int(input("Enter number of rows: "))

print("\nNormal Pyramid:")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2*i - 1))

print("\nReverse Pyramid:")
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2*i - 1))