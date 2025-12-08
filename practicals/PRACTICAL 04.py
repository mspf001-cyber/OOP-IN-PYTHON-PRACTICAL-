"""Practical 04: Character analysis"""

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character")
else:
    if char.isalpha():
        print(f"'{char}' is a {'uppercase' if char.isupper() else 'lowercase'} letter")
    elif char.isdigit():
        names = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
        print(f"'{char}' is a digit: {names[int(char)]}")
    else:
        print(f"'{char}' is a special character")