"""Practical 08: Cubes of even integers from list"""

lst = [1, 2, 3, 4, 5, 6, 'a', 7.5, 8, 9, 10]
print(f"Input list: {lst}")

# Method a: Using for loop
cubes_for = []
for item in lst:
    if isinstance(item, int) and item % 2 == 0:
        cubes_for.append(item ** 3)

# Method b: Using list comprehension
cubes_comp = [item**3 for item in lst if isinstance(item, int) and item % 2 == 0]

print(f"\nUsing for loop: {cubes_for}")
print(f"Using comprehension: {cubes_comp}")