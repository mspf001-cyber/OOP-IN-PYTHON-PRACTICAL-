"""Practical 07: Find all occurrences of substring"""

def find_occurrences(main_str, sub_str):
    indices, start = [], 0
    while True:
        idx = main_str.find(sub_str, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    return indices if indices else -1

main_str = input("Enter main string: ")
sub_str = input("Enter substring: ")

result = find_occurrences(main_str, sub_str)
print(f"Result: {result}")