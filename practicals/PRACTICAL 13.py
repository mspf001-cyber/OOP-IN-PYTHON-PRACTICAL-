"""Practical 13: Name validation with exception handling"""

class InvalidNameError(Exception):
    pass

try:
    name = input("Enter your name: ")
    
    if any(c.isdigit() for c in name):
        raise InvalidNameError("Name contains digits")
    
    if not all(c.isalpha() or c.isspace() for c in name):
        raise InvalidNameError("Name contains special characters")
    
    if not name.strip():
        raise InvalidNameError("Name cannot be empty")
    
    print(f"Valid name: {name}")

except InvalidNameError as e:
    print(f"Error: {e}")