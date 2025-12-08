"""Practical 12: Tuple operations"""

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print(f"Original tuple: {t1}")

# a) Print half values
mid = len(t1) // 2
print(f"\nFirst half: {t1[:mid]}")
print(f"Second half: {t1[mid:]}")

# b) Even numbers tuple
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print(f"\nEven numbers: {even_tuple}")

# c) Concatenate
t2 = (11, 13, 15)
t3 = t1 + t2
print(f"\nAfter concatenation: {t3}")

# d) Max and min
print(f"\nMaximum: {max(t1)}")
print(f"Minimum: {min(t1)}")