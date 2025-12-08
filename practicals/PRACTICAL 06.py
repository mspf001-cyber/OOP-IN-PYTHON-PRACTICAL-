"""Practical 06: Swap first n characters of two strings"""

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
n = int(input("Enter number of characters to swap: "))

if n > len(str1) or n > len(str2):
    print("Error: n exceeds string length")
else:
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    print(f"\nAfter swapping:")
    print(f"String 1: {new_str1}")
    print(f"String 2: {new_str2}")