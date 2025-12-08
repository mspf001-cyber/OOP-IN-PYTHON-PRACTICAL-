# 🐍 Python Programming Practicals

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Practicals](https://img.shields.io/badge/practicals-13-orange.svg)
![Status](https://img.shields.io/badge/status-complete-success.svg)

**Object Oriented Programming using Python**  
*B.Sc. (H) Computer Science - Semester I*  
*NEP UGCF 2022 | Academic Year 2025-26*

[About](#-about) • [Practicals](#-practical-list) • [Usage](#-usage) • [Topics](#-topics-covered)

</div>

---

## 📖 About

This repository contains **13 practical implementations** for the Object Oriented Programming using Python course (DSC01). Each practical is designed to be:

- ✅ **Concise** - Clean and minimal code
- ✅ **Functional** - Fully working solutions
- ✅ **Well-documented** - Clear comments and structure
- ✅ **Independent** - Each can run standalone

### 📚 Course Information

| Detail | Information |
|--------|-------------|
| **Course Code** | DSC01 |
| **Course Name** | Object Oriented Programming using Python |
| **Program** | B.Sc. (H) Computer Science |
| **Semester** | I |
| **Framework** | NEP UGCF 2022 |
| **Academic Year** | 2025-26 |
| **Institution** | Ramanujan College (University of Delhi) |

---

## 📝 Practical List

### Basic Programming (1-3)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **01** | Quadratic Equation | Find roots using discriminant | [`PRACTICAL 01.py`](practicals/PRACTICAL%2001.py) |
| **02** | Prime Numbers | Check prime, generate primes (with functions) | [`PRACTICAL 02.py`](practicals/PRACTICAL%2002.py) |
| **03** | Pyramid Patterns | Normal and reverse pyramid patterns | [`PRACTICAL 03.py`](practicals/PRACTICAL%2003.py) |

### String Operations (4-7)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **04** | Character Analysis | Identify character type and properties | [`PRACTICAL 04.py`](practicals/PRACTICAL%2004.py) |
| **05** | String Operations | Frequency, replace, remove operations | [`PRACTICAL 05.py`](practicals/PRACTICAL%2005.py) |
| **06** | Swap Characters | Swap first n characters of two strings | [`PRACTICAL 06.py`](practicals/PRACTICAL%2006.py) |
| **07** | Substring Search | Find all occurrences of substring | [`PRACTICAL 07.py`](practicals/PRACTICAL%2007.py) |

### Data Structures (8, 11-12)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **08** | List Comprehension | Cubes of even integers from mixed list | [`PRACTICAL 08.py`](practicals/PRACTICAL%2008.py) |
| **11** | Dictionary Operations | Create dictionary with cubes as values | [`PRACTICAL 11.py`](practicals/PRACTICAL%2011.py) |
| **12** | Tuple Operations | Slicing, filtering, concatenation, min/max | [`PRACTICAL 12.py`](practicals/PRACTICAL%2012.py) |

### Advanced Concepts (9-10, 13)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **09** | File Handling | Read, analyze, and manipulate file content | [`PRACTICAL 09.py`](practicals/PRACTICAL%2009.py) |
| **10** | OOP - Point Class | Class with attributes and distance method | [`PRACTICAL 10.py`](practicals/PRACTICAL%2010.py) |
| **13** | Exception Handling | Name validation with custom exceptions | [`PRACTICAL 13.py`](practicals/PRACTICAL%2013.py) |

---

## 💻 Usage

### Method 1: Run Individual Practical

```bash
# Run specific practical
python "practicals/PRACTICAL 01.py"
python "practicals/PRACTICAL 02.py"
# ... and so on
```

### Method 2: Interactive Menu

```bash
# Launch interactive menu
python main.py
```

**Menu Interface:**
```
============================================================
PYTHON PRACTICALS MENU
============================================================
 1. Practical 01
 2. Practical 02
 3. Practical 03
 ...
13. Practical 13
 0. Exit
============================================================
Enter choice: 
```

### Method 3: Import as Module

```python
# Import specific practical functions
import sys
sys.path.append('practicals')

# Now you can import (after adding .py files to practicals folder)
# Example: from a renamed file
```

---

## 📂 File Structure

```
python-oop-practicals/
│
├── 📄 README.md              # This file
├── 🐍 main.py                # Interactive menu
│
└── 📁 Practicals/
    ├── practical_01.py       # Quadratic equation
    ├── practical_02.py       # Prime numbers
    ├── practical_03.py       # Pyramid patterns
    ├── practical_04.py       # Character analysis
    ├── practical_05.py       # String operations
    ├── practical_06.py       # Swap characters
    ├── practical_07.py       # Substring search
    ├── practical_08.py       # List comprehension
    ├── practical_09.py       # File handling
    ├── practical_10.py       # Point class (OOP)
    ├── practical_11.py       # Dictionary operations
    ├── practical_12.py       # Tuple operations
    └── practical_13.py       # Exception handling
```

---

## 📚 Topics Covered

### 1. **Core Python Concepts**
- Variables and Data Types
- Input/Output Operations
- Control Structures (if-else, loops)
- Operators and Expressions

### 2. **Functions**
- Function Definition and Calls
- Parameters and Return Values
- Modular Programming
- Function Scope

### 3. **String Manipulation**
- String Methods
- String Slicing
- String Formatting
- Pattern Matching

### 4. **Data Structures**
- **Lists**: Creation, comprehension, manipulation
- **Tuples**: Immutable sequences, operations
- **Dictionaries**: Key-value pairs, methods
- **Sets**: Unique elements (bonus)

### 5. **File Handling**
- Reading from Files
- Writing to Files
- File Modes
- Context Managers (`with` statement)

### 6. **Object-Oriented Programming**
- Class Definition
- Objects and Instances
- Methods and Attributes
- `__init__` and `__str__` methods

### 7. **Exception Handling**
- Try-Except Blocks
- Custom Exceptions
- Error Handling Best Practices
- Input Validation

---

## 🎯 Learning Outcomes

After completing these practicals, you will be able to:

| Category | Skills Acquired |
|----------|----------------|
| **Programming Fundamentals** | Write clean, efficient Python code |
| **Problem Solving** | Break down complex problems into functions |
| **Data Structures** | Work with lists, tuples, dictionaries effectively |
| **OOP Concepts** | Design and implement classes and objects |
| **File Operations** | Read, write, and manipulate file data |
| **Error Handling** | Create robust programs with exception handling |

---

### Practice and Learning Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Practice Problems](https://www.hackerrank.com/domains/python)

---

## 🛠️ Technical Details

### Code Statistics

| Metric | Value |
|--------|-------|
| Total Files | 15 |
| Total Lines of Code | ~250 |
| Average File Size | 17 lines |
| Python Version | 3.6+ |
| External Dependencies | None |

### Code Quality

- ✅ PEP 8 Compliant
- ✅ Type hints (where applicable)
- ✅ Docstrings for functions
- ✅ Error handling implemented
- ✅ No external libraries required

---

## 👨‍💻 Author

**Birjesh Khatana**  
B.Sc. (H) Computer Science - Semester I  
Ramanujan College (University of Delhi)  
Academic Year: 2025-26

### Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/mspf001-cyber)

</div>

---

## 🙏 Acknowledgments

- Course Instructors at Ramanujan College (DU)
- Python Software Foundation for Python language
- GitHub for hosting this repository
- Classmates for collaborative learning

---


<div align="center">

**⚡️ Quick Links**

[Usage](#-usage) • [Practicals](#-practical-list) • [Topics](#-topics-covered)

---