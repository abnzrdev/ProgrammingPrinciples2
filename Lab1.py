# First Assignment
# Abenezer Alemayehu Lemma
# 6/3/2025

# Part 1: Python Basics

# Basic print statement
print("Hello, World!")  # This will print Hello, World

# Checking Python version
import sys
print(sys.version)

# Simple conditional statements
if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

# Variables and data types
x = 5
y = "Hello, World!"

# Single-line comment
# This is a comment.
print("Hello, World!")

# Multi-line comment
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# Assigning different data types to variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Type conversion
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Checking data types
x = 5
y = "John"
print(type(x))
print(type(y))

# Strings with different quotation marks
x = "John"
x = 'John'  # Same as above

# Variable names are case-sensitive
a = 4
A = "Sally"  # A will not overwrite a

# Valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Naming conventions
myVariableName = "John"  # Camel case
MyVariableName = "John"  # Pascal case
my_variable_name = "John"  # Snake case

# Assigning the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Assigning multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Part 2: Python

# Integer type
x = 1
print(type(x))

# Large integer
y = 35656222554887711
print(type(y))

# Negative integer
z = -3255522
print(type(z))

# Float type
x = 1.10
print(type(x))

y = 1.0
print(type(y))

z = -35.59
print(type(z))

# Scientific notation (float)
x = 35e3
print(type(x))

y = 12E4
print(type(y))

z = -87.7e100
print(type(z))

# Complex numbers
x = 3+5j
print(type(x))

y = 5j
print(type(y))

z = -5j
print(type(z))

# Type conversions between int, float, complex
a = float(1)
print(a, type(a))

b = int(2.8)
print(b, type(b))

c = complex(1)
print(c, type(c))

# Random number between 1 and 9
import random
print(random.randrange(1, 10))

# Type casting
x = int(1)
y = int(2.8)
z = int("3")

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

x = str("s1")
y = str(2)
z = str(3.0)

