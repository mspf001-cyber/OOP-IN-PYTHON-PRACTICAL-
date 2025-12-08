# 🐍 Python Programming Practicals

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Practicals](https://img.shields.io/badge/practicals-13-orange.svg)
![Status](https://img.shields.io/badge/status-complete-success.svg)

**Object Oriented Programming using Python**  
*B.Sc. (H) Computer Science - Semester I*  
*NEP UGCF 2022 | Academic Year 2025-26*

[About](#-about) • [Practicals](#-practical-list) • [Installation](#-installation) • [Usage](#-usage) • [Topics](#-topics-covered)

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

---

## 📝 Practical List

### Basic Programming (1-3)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **01** | Quadratic Equation | Find roots using discriminant | [`practical_01.py`](practical_01.py) |
| **02** | Prime Numbers | Check prime, generate primes (with functions) | [`practical_02.py`](practical_02.py) |
| **03** | Pyramid Patterns | Normal and reverse pyramid patterns | [`practical_03.py`](practical_03.py) |

### String Operations (4-7)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **04** | Character Analysis | Identify character type and properties | [`practical_04.py`](practical_04.py) |
| **05** | String Operations | Frequency, replace, remove operations | [`practical_05.py`](practical_05.py) |
| **06** | Swap Characters | Swap first n characters of two strings | [`practical_06.py`](practical_06.py) |
| **07** | Substring Search | Find all occurrences of substring | [`practical_07.py`](practical_07.py) |

### Data Structures (8, 11-12)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **08** | List Comprehension | Cubes of even integers from mixed list | [`practical_08.py`](practical_08.py) |
| **11** | Dictionary Operations | Create dictionary with cubes as values | [`practical_11.py`](practical_11.py) |
| **12** | Tuple Operations | Slicing, filtering, concatenation, min/max | [`practical_12.py`](practical_12.py) |

### Advanced Concepts (9-10, 13)

| # | Practical Name | Description | File |
|---|----------------|-------------|------|
| **09** | File Handling | Read, analyze, and manipulate file content | [`practical_09.py`](practical_09.py) |
| **10** | OOP - Point Class | Class with attributes and distance method | [`practical_10.py`](practical_10.py) |
| **13** | Exception Handling | Name validation with custom exceptions | [`practical_13.py`](practical_13.py) |

---

## 🚀 Installation

### Prerequisites

```bash
# Check Python version (3.6+ required)
python --version
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
from practical_02 import is_prime, first_n_primes

# Use the functions
print(is_prime(17))  # True
print(first_n_primes(5))  # [2, 3, 5, 7, 11]
```

---

## 📂 File Structure

```
python-oop-practicals/
│
├── 📄 README.md              # This file
├── 🐍 main.py                # Interactive menu
│
├── 📁 Practicals/
│   ├── practical_01.py       # Quadratic equation
│   ├── practical_02.py       # Prime numbers
│   ├── practical_03.py       # Pyramid patterns
│   ├── practical_04.py       # Character analysis
│   ├── practical_05.py       # String operations
│   ├── practical_06.py       # Swap characters
│   ├── practical_07.py       # Substring search
│   ├── practical_08.py       # List comprehension
│   ├── practical_09.py       # File handling
│   ├── practical_10.py       # Point class (OOP)
│   ├── practical_11.py       # Dictionary operations
│   ├── practical_12.py       # Tuple operations
│   └── practical_13.py       # Exception handling
│
└── 📜 LICENSE                # MIT License
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

## Supplementary Resources

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
- ✅ Err