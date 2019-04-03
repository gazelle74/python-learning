############################################
# A 45 Minute Hands-On Python Crash Course
# What to expect:
# -- Intro to variables, data types, and IDEs
# -- print() function
# -- operators
# -- strings and their properties
# -- boolean types in python
# -- control flow
# -- iteration
# -- classes and OOP
# -- data structures
# -- scripting in python
#
# 3 SIMPLE GOALS
# ----------------
# To create and run a python file
# To make simple 'tweaks' to this python doc
# To empower you to continue your python education
#
# By Doug Purcell
# Website: http://www.purcellconsult.com
#
#
#############################################

# PYTHON INSTALLATION
# _ _ _ _ _ _ _ _ _ _
#
# Tutorial for installation on Windows, Mac Os, and Linux: http://purcellconsult.com/python-installation-tutorial
# online python interpreter: https://repl.it/languages/python3

# VARIABLES
# ---------------------------------------------------------
# python variables, number types, and IDEs

a = 10
b = 1.598
c = .1987
d = 100.579


# print()
# ---------------------------------------------------------------
# the print() function in python3.0 displays output to the console

print(a)
print(b)
print(c)
print(d)


# How to run a python file
# In PyCharm click Run -> Run -> Name of the file
# Or, use the pycharm shortcut: Alt+Shift+F10

# swapping variables

x = 5
y = 10
z = 30
x, y, z = z, x, y
print(x)
print(y)
print(z)

# Variable naming tips: PEP 8 - Style Guide for Python Code
    # var names can have letters, numbers, and underscores
    # can't use a reserved word like 'print'
    # try and be as descriptive as possible. Makes code more maintainable
    # python IS case sensitive.
    # put constants in all CAPS: DAYS_OF_WEEK = 7


# PYTHON MATH OPERATORS: +, -, *, **,  / , //, %
# -----------------------------------------------
# python can be used as a 'souped-up' calculator

print(10 + 10)
print(50 - 10)
print(10 * 10)
print(20 ** 2)
print(9 / 5)
print(8 // 3)
print(11 % 5)
print(1e10)

# For more advanced math operations use
# The builtin 'math' module

import math

print(math.log(1000000, 2))
print(math.sqrt(9))
print(math.cos(100) + math.sin(90) + math.tan(90))
print(math.pi**2 * math.e)

# STRINGS
# --------------------------------------
# Think SMS text, Facebook chat, MS Word, emails, or even emojis
# Strings can be single quote (''), double quote ("") or triple quote (""")

city = 'Los Angeles'

# indexing: python is a zero based indexed language
print(city[0])  # L
print(city[3])  # empty space is a string!
print(city[4])  # capital A
print(city[-1]) # negative indices are permitted

# len() function: gets the length of the string
print(len(city))    # 11
print(city[len(city)-1]) # s

# concatenation: the combining of multiple strings
print('john ' + 'doe ' + 'public')

# slicing: retrieves ranges of a string
print(city[0:3])   # Los
print(city[4:11])  # Angeles
print(city[::])    # Los Angeles
print(city[::2])   # LsAgls
print(city[::-1])  # selegnA soL

# BOOLEAN ALGEBRA: True or False
# ----------------------------------------
# Should understand truth tables
# Used to determine control flow: if/elif/else statements
# Describe boolean type by asking true or false questions

is_the_sky_blue = True
do_cats_bark = False

print(is_the_sky_blue)
print(do_cats_bark)

# The 'and' truth table
# 'and' evaluates to false unless both operands are False

print(True and True)
print(True and False)
print(False and False)
print(False and True)

# or evaluates to true with at least one true operand
print(True or True)
print(True or False)
print(False or False)
print(False or True)

# xor evaluates to true
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)


# CONTROL FLOW IN PYTHON
# -----------------------
# if/else statement

x, y, z = 5, 10, 15
if x < y and z > y:
    print(x)
else:
    print(y)

# elif statement
from random import randint

# picks a random number in range 1...100
grade = randint(1, 100)
if grade >= 90 <= 100:
    print('A')
elif grade >= 80 <= 89.9:
    print('B')
elif grade >= 70 <= 79.9:
    print('C')
elif grade >= 60 <= 69.9:
    print('D')
else:
    print('F!')

# ternary statement
mood = True
state = 'nice' if mood else 'not so nice'
print('state = {}'.format(state))

# ITERATION IN PYTHON
# ----------------------
# allows us to compute repeated tasks.
# computers are amazing at this!

# WHILE LOOP

# sets while loop starting at
i = 0
# condition
while i < 10:
    print('i =  {}'.format(i, end=' '))  # print value of i, end='' means print on same line
    i += 1  # increment i

# sum numbers from 1...1000 in nanoseconds
i, sum = 0, 0
while i < 1000:
    i += 1
    sum += i
print('The summation of 1...1000 = {}'.format(sum))

# for loop
for x in range(10):
    print(x, end=' ')

# fibonacci number
print()
x, y = 0, 1
for z in range(10):
    next = x + y
    x, y = y, next
print('12th fib number = {}'.format(next))


# creating functions
# a functions maps a set of inputs to outputs.
# You can create your own using the 'def' keyword in python

def scale_number(num, amount):
    return num * amount

print(scale_number(10, 5))

# keyword arguments


def area_triangle(height=11, width=7.5):
    return 1/2 * (height * width)


print(area_triangle())
print(area_triangle(height=20, width=100))

# can accept an arbitrary number of input


def multiply(*args, y=1):

    for x in range(len(args)):
        y *= args[x]
    return y

print('multiply=', multiply(1, 2, 3, 4))

print()

def key_value(**kwargs):
    for key, value in kwargs.items():
        print('{} {}'.format(key, value))

key_value(a=5, b=10, c=15)




# classes and objects
# classes are used to model real world objects 

class Point:
    """Simple class in python. This is an example
    of a docstring, or a string that's used like a
    comment to document a segment of code."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_point(self):
        return self.x, self.y


p = Point(5, 10)
print()
print(p.get_point())
p.set_x(100)
p.set_y(200)
print(p.get_point())

# list are mutable collection of objects
evens = [0, 2, 4, 6, 8, 10]
# reverses the list
evens.reverse()
# adds an object to the list
evens.append(100)
# merges another list with the list
evens.extend([1, 3, 5, 7, 9])
# pops an item from the list
evens.pop()
# iterating over a list
for x in evens:
    print(x)

# tuples
# immutable sequence
nums = (1, 3, 5, 7)
print(nums)

# dictionaries
# key/value pairs, or associative arrays in some languages.
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for key, value in vowels.items():
    print(key, value)

# sets
# stores unique items
letters = {'a', 'a', 'a', 'b', 'b', 'b'}
print(sorted(letters))
