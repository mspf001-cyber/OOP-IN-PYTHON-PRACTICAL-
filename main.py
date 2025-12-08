"""Main Menu for Python Practicals"""

import os
import sys

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_practical(choice):
    """Run selected practical based on user choice"""
    
    # Map choices to filenames (in practicals folder)
    practicals = {
        '1': 'practicals/PRACTICAL 01.py',
        '2': 'practicals/PRACTICAL 02.py',
        '3': 'practicals/PRACTICAL 03.py',
        '4': 'practicals/PRACTICAL 04.py',
        '5': 'practicals/PRACTICAL 05.py',
        '6': 'practicals/PRACTICAL 06.py',
        '7': 'practicals/PRACTICAL 07.py',
        '8': 'practicals/PRACTICAL 08.py',
        '9': 'practicals/PRACTICAL 09.py',
        '10': 'practicals/PRACTICAL 10.py',
        '11': 'practicals/PRACTICAL 11.py',
        '12': 'practicals/PRACTICAL 12.py',
        '13': 'practicals/PRACTICAL 13.py'
    }
    
    if choice == '0':
        return False
    
    if choice in practicals:
        filename = practicals[choice]
        
        if os.path.exists(filename):
            print(f"\n{'='*60}")
            print(f"Running: {filename}")
            print('='*60)
            print()
            
            os.system(f'python "{filename}"')
            
            print("\n" + "="*60)
            input("Press Enter to return to menu...")
        else:
            print(f"\n❌ Error: '{filename}' not found!")
            input("Press Enter to continue...")
    else:
        print("\n❌ Invalid choice! Enter 0-13")
        input("Press Enter to continue...")
    
    return True

def display_menu():
    """Display main menu"""
    clear_screen()
    print("="*60)
    print(" "*15 + "PYTHON PRACTICALS MENU")
    print("="*60)
    print("\n  No.  Practical Name")
    print("-"*60)
    print("  01.  Quadratic Equation Roots")
    print("  02.  Prime Number Operations")
    print("  03.  Pyramid Patterns")
    print("  04.  Character Analysis")
    print("  05.  String Operations")
    print("  06.  Swap String Characters")
    print("  07.  Find Substring Occurrences")
    print("  08.  Cubes of Even Integers")
    print("  09.  File Operations")
    print("  10.  Point Class (OOP)")
    print("  11.  Dictionary with Cubes")
    print("  12.  Tuple Operations")
    print("  13.  Name Validation")
    print("-"*60)
    print("  0.   Exit")
    print("="*60)

def main():
    """Main function"""
    while True:
        display_menu()
        choice = input("\n👉 Enter choice (0-13): ").strip()
        
        if not run_practical(choice):
            clear_screen()
            print("\n" + "="*60)
            print(" "*20 + "THANK YOU!")
            print("="*60)
            print("\n  ✅ Program completed!")
            print("  📚 Keep coding!")
            print("\n" + "="*60 + "\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user\n")
        sys.exit(0)