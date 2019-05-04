
"""
    Python - Variable
"""


"""
What is Variable ?
Variables are nothing but reserved memory locations to store values.

"""


# How to Assigning Values to Variables ?
# the equal sign (=) is used to assign values to variables.

x = 10
print(x)

y = "Hello"
print(y)

z = 69.69
print(z)
print('\n')

# Example

a = 5
b = 6
ab = a * b
print("ab : ", ab)

# Swap Variable

print("Swap Variable :- \n")

# 2 way to Swap Variable

# Example
a = 5
print("a : ", a)
b = 6
print("b : ", b)
temp = a
a = b
b = temp
print("Swap a : ", a)
print("Swap b : ", b)
print("\n")

# Example of Swap Variable

a = 10
print("a : ", a)
b = 13
print("b : ", b)
a = a + b
b = a - b
a = a - b

print("Swap a : ", a)
print("Swap b : ", b)
print("\n")


# Swap in Pythonic way?

print("Swapping Values in Python : ")
a = 69
print("a : ", a)
b = 10
print("b : ", b)
a, b = b, a
print("Swap a : ", a)
print("Swap b : ", b)
print("\n")


# Multiple Assignment
a = b = c = 69
print(a)
print(b)
print(c)


# More Example

a, b, c = 1, 2, "jibon"
print(a)
print(b)
print(c)
print('\n')

# Example

x = (
    2 + 4 * 6 -
    6 + 4 - 2 +
    3 - 3 * 4
)
print("X : ", x)
print('\n')

# Now Learn Variable

"""
name (char, string, boolean) number (int, float, double, long)
"""

# Example

# Here x is variable and values is "My variable"

x = "My variable"
print(x)

# Example
a = 4
print("a : ", a)
print('\n')


# Example

A = 4
print("A : ", A)
print("\n")

# Example

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

"""
A constant is a type of variable whose value cannot be changed.
"""

PI = 3.14
print("PI : ", PI)
print('\n')

# Example

GRAVITY = 9.8
print("GRAVITY : ", GRAVITY)
print('\n')


# Example of Numeric Literals

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

print("Binary Literals     : ", a)
print("Decimal Literal     : ", b)
print("Octal Literal       : ", c)
print("Hexadecimal Literal : ", d)
print('\n')

"""
>>> a = 0b1010
>>> a
10
>>> bin(10)
'0b1010'
>>> 
"""

# Example of Complex Literal

x = 3.14j
print(x)
print(x, x.imag, x.real)
print('\n')

# Example of Float Literal

float_1 = 10.5
float_2 = 1.5e2

print(float_1)
print(float_2)
print('\n')

# Example of memory address or Location

a = 6.9
print(a)
print(id(a))  # id means memory Location


# Write a program to find out your Age

user_input = input("Enter your Age : ")

Age = 2019 - int(user_input)

print("You Are " + str(Age) + " years old")

print('\n')


print("Best of luck .... And keep Coding.....")
