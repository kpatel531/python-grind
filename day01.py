# python is dynamic typed.

# comments: [use to explain code not involve in execution]
# single line, inline, multiple line and Unassigned String Literals (Docstrings) Like (""") and (''')

# Variable
"""
Topic: Variable
Defination: Container that store a data and point that value and that can referenced and manipulated during program execution.
Program:
"""

age = 25
name = "Kaushal"

print(age)
print(name)
"""
O/P:
25
Kaushal
"""

x = 10 # x is an integer
x = "Hello python" # x is now a string with manipulated data and type

print(x)
"""
O/P:
Hello python
"""
# Multiple values to multiple variables:
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

"""
O/P:
Apple
Banana
Cherry
"""
# Same value to multiple variables:
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""
O/P:
Orange
Orange
Orange
"""
# Swapping two variables:(without using temporary varible)
a = 1
b = 2
a, b = b, a  # Now a is 2, and b is 1
print(a)
print(b)

"""
O/P:
2
1
"""

# String
"""
Topic: String
Defination: String is collection of unicode characters in form of bond list.
Program:
"""

single_str = 'Hello, world'
double_str = "Python programming"

# Mutiple line string
multiline_str = """This is a string that
contains multiple
line of code values.
"""

print(single_str)
print(double_str)
print(multiline_str)

"""
O/P:
Hello, world
Python programming
This is a string that
contains multiple
line of code values.
"""

# string {Indexing and Slicing}
'''Since, string is collection of characters that uniform in list. 
That always starts at position of 0. where negative index will follow at end.'''
text = "Python"

## Indexing
print(text[0])   # Output: 'P'
print(text[-1])   # Output: 'n'

## Slicing
print(text[0:4]) # Output: 'Pyth' (indices 0, 1, 2, 3)
print(text[2:])  # Output: 'thon' (index 2 to the end)
print(text[::-1]) # Output: 'nohtyP' (reverses the string)

# String Formatting

name = "Kaushal"
age = 25

# Using f-strings (recommended)
greeting = f"My name is {name} and I am {age} years old." 

# Using .format()
greeting_alt = "My name is {} and I am {} years old.".format(name, age)

print(greeting)
print(greeting_alt)


# Common String Operations & Methods
print("Hello " + "World") # Concatenates (combines) two strings. [+ Operator] O/P => "Hello World"
print("Hi!" * 3) # Repeats a string a given number of times. [* Operator] O/P => "Hi!Hi!Hi!"
print(len("cat")) # Returns the total character count (including spaces). [len(str)]  O/P => 3
print("Python".upper()) # Converts text entirely to uppercase [.upper()] O/P => "PYTHON"
print("Python".lower()) # Converts text entirely to lowercase [.lower()] O/P => "python"
print("  hello  ".strip()) # Removes leading and trailing whitespace. [.strip()] O/P => "hello"
print("bat".replace("b", "c")) # Replaces occurrences of a substring with another. [.replace(old, new)] O/P => "cat"
print("banana".find("na")) # Returns the lowest index where the substring is found, or -1. [.find(sub)] O/P => 2
print("plan" in "planet") # Evaluates True if a substring exists within the text. [in Operator] O/P => True

# Number
"""
Topic: Number
Defination: Number are used to store numeric values and perform mathematical operations.
Program:
"""

x = 10
y = 10.5
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>


# complex number: Numbers written with a j or J representing the imaginary part.
# Type Coversion (Casting)
x = 3.8
y = 5

# Convert float to int (truncates the decimal)
print(int(x))      # Output: 3

# Convert int to float
print(float(y))    # Output: 5.0

# Convert int to complex
print(complex(y))  # Output: (5+0j)


# Numbers: Arithmetic Operations

"""
Addition (+): 5 + 3 → 8
Subtraction (-): 10 - 2 → 8
Multiplication (*): 4 * 2 → 8
Division (/): Always returns a float, even if the numbers divide evenly (9 / 3 → 3.0).
Floor Division (//): Divides and rounds down to the nearest whole number (10 // 3 → 3).
Modulus (%): Returns the division remainder (10 % 3 → 1).
Exponentiation (**): Raises a number to a power (2 ** 3 → 8).
"""