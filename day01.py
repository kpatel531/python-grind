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

# Boolean
"""
Topic: Boolean
Defination: A boolean value is either True or False.
Program:
"""

# Creating boolean variables
is_true = True
has_error = False

print(type(is_true))  # Output: <class 'bool'>

# Comparison Operators
print(5 == 5)  # Output: True
print(5 != 5)  # Output: False
print(5 > 3)   # Output: True
print(5 < 3)   # Output: False
print(5 >= 5)  # Output: True
print(5 <= 3)  # Output: False

# Logical Operators (Combining boolean values)
print(is_true and has_error)  # Output: False
print(is_true or has_error)   # Output: True
print(not is_true)            # Output: False

# Advanced not: Booleans are integers in Python, where True is 1 and False is 0. This allows for arithmetic operations with boolean values.
print(True + True)   # Output: 2
print(False + False) # Output: 0

# Type conversion (Casting)
"""
Topic: Type Conversion
Defination: Type conversion is the process of converting a value from one data type to another.
Program:
"""

# Implicit Type Conversion (Type Casting) Conversion: Python automatically converts one data type to another when necessary.
num1 = 10      # int
num2 = 5.5     # float
result = num1 + num2  # Implicit conversion: int is converted to float
print(result)  # Output: 15.5
print(type(result))  # Output: <class 'float'>

# Explicit Type Conversion (Type Casting) Conversion: The programmer manually converts a value from one data type to another using built-in functions.
num_str = "100"
num_int = int(num_str)  # Explicit conversion from string to int
print(num_int)  # Output: 100

num_float = float(num_int)  # Explicit conversion from int to float
print(num_float)  # Output: 100.0

num_complex = complex(num_float)  # Explicit conversion from float to complex
print(num_complex)  # Output: (100+0j)

num_bool = bool(num_int)  # Explicit conversion from int to bool
print(num_bool)  # Output: True


# Input
"""
Topic: Input
Defination: Input is a way to get data from the user during program execution.
Program:
"""

# Basic Input
user_input = input("Enter something: ")
print("You entered:", user_input)

# Type Conversion with Input
age = int(input("Enter your age: "))
print("Your age is:", age)

price = float(input("Enter the price: "))
print("The price is:", price)

# Splitting Input
numbers = input("Enter numbers separated by spaces: ")
number_list = numbers.split()
print("The numbers are:", number_list)

# Comparison operators
"""
Topic: Comparison Operators
Defination: Comparison operators are used to compare two values and return a boolean result (True or False).
Program:
"""

print(5 == 5)  # Output: True
print(5 != 3)  # Output: True   
print(5 > 3)   # Output: True
print(5 < 3)   # Output: False
print(5 >= 5)  # Output: True
print(5 <= 3)  # Output: False
print(5 == 5.0)  # Output: True (int and float comparison)
print(5 is "5")  # Output: False

# logical operators
"""
Topic: Logical Operators
Defination: Logical operators are used to combine conditional statements and return a boolean result (True or
    False).
Program:
"""

print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# if / elif / else
"""
Topic: if / elif / else
Defination: The if statement is used to execute a block of code if a condition is true. The elif statement is used to check another condition if the previous condition is false. The else statement is used to execute a block of code if all previous conditions are false.
Program:
"""

print("Enter a number:")
num = int(input())
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Loops
"""
Topic: Loops
Defination: Loops are used to execute a block of code repeatedly as long as a condition
is true. Python has two main types of loops: for loops and while loops.
Program:
"""

# for loop
for i in range(5):  # Loop from 0 to 4
    print("Iteration:", i)

# while loop
counter = 0
while counter < 5:  # Loop until counter is less than 5
    print("Counter:", counter)
    counter += 1  # Increment counter by 1

# Loop Control Statements
"""
break: Exits the loop immediately.
continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
"""


# For Loop: A for loop is used to iterate over a sequence or an iterable object (such as a list, tuple, string, dictionary, or range). It executes a fixed number of times based on the size of the sequence.
for i in range(10):
    if i == 3:
            continue  # Skip this current iteration when i is 3
    if i == 5:
        break  # Exit the loop when i is 5
    print("Current value:", i)


# While Loop: A while loop executes a block of code as long as a specific boolean condition remains True. It is typically used when the exact number of iterations is not known beforehand.
count = 0
while count < 5:
    print(count)
    count += 1 # Crucial to update the condition to avoid an infinite loop


# Lists
"""
Topic: Lists
Defination: list is a built-in, ordered, and mutable collection of items enclosed in square brackets [].
    non-primitive data structure which hold mulriple types of data init.
Program:
"""

# Creating a list: You can define a list by placing comma-separated values inside square brackets, or by using the built-in list() constructor

# Empty list
empty_lst = []
print(empty_lst)

# List with items
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_lst = ["Python", 3.14, True, 42]
print(mixed_lst)

# Using the list() constructor
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
print(chars)


# List. Accessing Elements (Indexing & Slicing)
#: Python uses zero-based indexing, meaning the first item is at index 0. You can also use negative indexing to access items starting from the end of the list (-1 represents the last item).

planets = ["Mercury", "Venus", "Earth", "Mars"]

print(planets[0])   # Output: Mercury
print(planets[-1])  # Output: Mars (last item)

# Slicing: [start:stop] extracts a portion of the list
print(planets[1:3]) # Output: ['Venus', 'Earth']



# List. Modifying Elements
#. Because lists are mutable, you can change their contents directly by referencing their index

numbers = [10, 20, 30]
numbers[1] = 99
print(numbers) # Output: [10, 99, 30]


# Common List Methods & Operations : Python provides several built-in methods to manipulate lists
'''
Adding Items
   - .append(item): Adds an item to the end of the list.
   - .insert(index, item): Inserts an item at a specific position.
   - .extend(iterable): Appends multiple elements (like another list) to the end.
'''

items = ["a", "b"]
items.append("c")       # ['a', 'b', 'c']
items.insert(1, "z")    # ['a', 'z', 'b', 'c']
items.extend(["d", "e"]) # ['a', 'z', 'b', 'c', 'd', 'e']

'''
Removing Items
    - .pop(index): Removes and returns the item at the given index. If no index is provided, it removes the last item.
    - .remove(item): Removes the first occurrence of a specific value.
    - .clear(): Removes all items from the list.
'''
items = ["a", "b", "c", "b"]
items.pop()        # Removes 'b' and returns it
items.remove("b")  # Removes the first 'b'
print(items)       # Output: ['a', 'c']

'''
Utility Methods
    - len(list): Built-in function that returns the total number of elements.
    - .sort(): Sorts the list in place (ascending order by default).
    - .reverse(): Reverses the elements of the list in place.
'''
# Ascending order (Default)
numbers = [4, 2, 5, 1, 3]
numbers.sort()
print(numbers)
# Output: [1, 2, 3, 4, 5]

# Descending order
numbers.sort(reverse=True)
print(numbers)
# Output: [5, 4, 3, 2, 1]

#  Iterating Through a List: You can easily loop through the items of a list using a for loop
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

