
# Start :-  11:41 AM 6/10/2019

# Python Variable


# What is Variable ?

"""
Variables are nothing but reserved memory locations to store values.
or
Variable -- হোল একটি বক্স যার মধ্যে আমারা আনেক কিছু রাখতে পারি ।
"""

# Variable are two types Name, Number

"""
1. Name   : char, string, boolean
2. Number : int, float, double, long
"""

# Rules of variable

"""
    ১. প্রতিটি variable ভেরিয়েবল এর একটি নাম থাকতে হবে ।
    ২. প্রথম লিটার আবশ্যই alphabetic letter আথাৎ uppercase or lowercase or underscore হতে হবে । A, a, _variable ।
    ৩. Symbols দ্বারা শুরু হতে পারবেনা । @, #, $, %, ! ... ।
    ৪. কোন স সংখ্য দ্বারা হতে পারবেনা ।
    ৫. এর শেষে ; দিতে হয় না ।
    ৬. Python case sensitive আথাৎ a = 4 and A = 4 same না ।
    ৭. Python data type  বলে দিতে হয় না । 
    ৮. Reserved keyword দ্বারা শুরু হতে পারবেনা । 
"""

# How to Assigning Values to Variables ?
# the equal sign (=) is used to assign values to variables.

# Example

# How to Assigning Values to Variables ?
# the equal sign (=) is used to assign values to variables.

a = 5  # Here a is variable and 5 is value.
print(a)

y = "Hello"  # Here y is variable and "Hello" is value.
print(y)

c = 69.69  # Here c is variable and 69.69 is value.
print(c)
print('\n')


# Example if a = 5 and b = 10 then ab = ?

a = 5
b = 6
ab = a * b
print("ab : ", ab)
print("\n")


# Example of multiple assignment

A, B, C = 10, 20, 30

print("A = : ", A)
print("B = : ", B)
print("C = : ", C)
print('\n')

# Example

a = b = c = 69

print("a = : ", a)
print("b = : ", b)
print("c = : ", c)
print("\n")


# Multiple line sum

a = (
    4 + 6 + 3 -
    3 + 2 * 4 +
    10/2 * 2 + 10
)
print("Multiple line = ", a)
print('\n')


# Swap Variable

print("Swap Variable :- \n")

a = 5
b = 6
print('a = ', a)
print('b = ', b)

a, b = b, a

print("Swap a : ", a)
print("Swap b : ", b)
print("\n")


# Example

name = "Python"
Age = 23
_Location = "69/A"
ADDRESS = "Dhaka"

print("Name     : ", name)
print("Age      : ", Age)
print("Location : ", _Location)
print("Address  : ", ADDRESS)
print("\n")


# Example of Constants

# A constant is a type of variable whose value cannot be changed.

PI = 3.14
print("PI : ", PI)

# Example

GRAVITY = 9.8
print("GRAVITY : ", GRAVITY)
print('\n')


# Example of Numeric Literals

a = 0b1010  # Binary Literals
b = 100     # Decimal Literal
c = 0o310   # Octal Literal
d = 0x12c   # Hexadecimal Literal

print("Binary Literals     : ", a)
print("Decimal Literal     : ", b)
print("Octal Literal       : ", c)
print("Hexadecimal Literal : ", d)
print('\n')


# Example of Complex Literal

x = 3 + 4j
print(x)
print("img number = ", x.imag)
print("real number = ", x.real)
print('\n')


# Example of Float Literal

float_1 = 10.5
float_2 = 1.5e2

print(float_1)
print(float_2)
print('\n')


