"""Practical 05: String operations"""

string = input("Enter a string: ")
char = input("Enter a character to operate on: ")

print(f"\na) Frequency of '{char}': {string.count(char)}")

new_char = input("b) Replace with: ")
print(f"   After replacement: {string.replace(char, new_char)}")

print(f"c) Remove first occurrence: {string.replace(char, '', 1)}")
print(f"d) Remove all occurrences: {string.replace(char, '')}")