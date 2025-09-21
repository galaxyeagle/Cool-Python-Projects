# -*- coding: utf-8 -*-
"""Modules.ipynb
    💡 To run this notebook properly: 

        1. Open in Google Colab 
        2. Uncomment the magic commands (%%writefile, !mkdir) in each cell.
        3. Run cells one by one.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile math_utils.py
# """
# A simple module containing reusable math functions.
# """
# 
# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
# 
# def multiply(a, b):
#     """Returns the product of two numbers."""
#     return a * b
# 
# def greet(name):
#     """Returns a greeting message."""
#     return f"Hello, {name}!"

# Importing and using the module
import math_utils

print("=== MODULE DEMO ===")
result1 = math_utils.add(5, 3)
result2 = math_utils.multiply(4, 7)
greeting = math_utils.greet("Alice")

print(f"5 + 3 = {result1}")
print(f"4 * 7 = {result2}")
print(greeting)

# First, create the package structure
!mkdir -p mypackage

# Commented out IPython magic to ensure Python compatibility.
# %%writefile mypackage/__init__.py
# """
# This file makes 'mypackage' a Python package.
# You can initialize package-level variables or control imports here.
# """
# __version__ = "1.0.0"

# Commented out IPython magic to ensure Python compatibility.
# %%writefile mypackage/string_utils.py
# """
# Module for string manipulation within the mypackage.
# """
# 
# def reverse_string(s):
#     """Returns the reversed string."""
#     return s[::-1]
# 
# def count_vowels(s):
#     """Returns the number of vowels in the string."""
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)

# Using the package
from mypackage import string_utils
import mypackage

print("\n=== PACKAGE DEMO ===")
print(f"Package Version: {mypackage.__version__}")

original = "Hello World"
reversed_str = string_utils.reverse_string(original)
vowel_count = string_utils.count_vowels(original)

print(f"Original: {original}")
print(f"Reversed: {reversed_str}")
print(f"Vowel Count: {vowel_count}")

print("\n=== LIBRARY vs FRAMEWORK ===")
print("""
LIBRARY:
- A collection of pre-written code (modules/packages) for specific tasks.
- You call the library's functions when YOU need them.
- Example: `requests` library for HTTP requests.

FRAMEWORK:
- A complete structure or environment for building applications.
- The framework calls YOUR code (Inversion of Control).
- Example: `Django` for web applications.

Use a LIBRARY when you need a helper tool (e.g., regex, NumPy).
Use a FRAMEWORK when building a large, structured project (e.g., web app, ML pipeline).
""")
