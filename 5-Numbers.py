

# Number in Python

# Basic Operations + , - , * , %
"""
>>> # পাইথনের কনসোলে সহজেই ম্যাথেম্যাটিক্যাল ক্যালকুলেশন করা যায়।
>>> 3 + 5
8
"""
# Example of Addition
x = 2 + 4
print(x)


# Example of Subtraction
x = 2 - 4
print(x)


# Example of Multiplication
x = 2 * 4
print(x)


# Example of Division
x = 6 / 2
print(x)


# Example of Remainder
x = 6 % 2
print(x)


# যোগ বিয়োগের মতই গুন ভাগের কাজও এখানে সহজেই করা যায়।

x = (2 + 2 / 3 - 4)
print(x)


# Example
x = 50 - (3 + 3 * 2)
print(x)


#  নাম্বারের আগে মাইনাস (-) সাইন দিয়ে নেগেটিভ নাম্বার নির্ধারণ করে দেয়া হয়।

x = -9 + 2
print("Negative int x : ", x)



# Example
"""
>>> # সাধারণ গণিতের মতই পাইথনে কোন সংখ্যাকে শূন্য দিয়ে ভাগ করতে গেলে এরর আসবে
>>> 45/0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    45/0
ZeroDivisionError: division by zero
"""


# Example
"""
যোগ, বিয়োগ, গুন ভাগ বাদেও পাইথনে Exponentiation or power এর সাপোর্ট আছে 
যাকে আমরা একটি সংখ্যার উপর আরেকটা সংখ্যার পাওয়ার বলে থাকি।
"""


# Example

x = 2**3
print("Power of x :", x)


# floor division ভাগশেষ নির্ণয়ের জন্য ব্যবহার করা হয়।

x = 10 // 3
print("floor division of x : ", x)


# দশমিক চিহ্ন ব্যবহার করা মানেই হল সেটি একটি float

x = 6.9
print("float of x : ", x)
print('\n')


# Python supports four different numerical types Numbers
"""
int (signed integers)
long (long integers )
float (floating point real values)
complex (complex numbers)

"""
'''
Python supports integers, floating point numbers and complex numbers. 
They are defined as int, float and complex class in Python.
Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

'''


# Example of integers

a = 5
print(a)
print(type(a))
print("\n")


# floating point numbers
x = 7.0
print(x)
print(type(x))
print("\n")


# Example Complex numbers
y = 7 + 6j
print(y)
print("real number       : ", y.real)
print("imaginary number  : ", y.imag)
print(isinstance(y, complex))  # isinstance() function to check if it belongs to a particular class
print("\n")



# Example of Advanced Numbers
# Hexadecimal
print("Example of Hexadecimal")
x = hex(246)
print("Hexadecimal of x :", x)



# Example
x = hex(512)
print("Hexadecimal of x :", x)
print('\n')

print("Example of Binary")
# Using the function bin() you can convert numbers into their binary format.

x = bin(1234)
print("Binary of 1234 :", x)


# Example
x = bin(128)
print("Binary of 128  :", x)
print('\n')



print("Example of pow()")
# pow()
# With two arguments, equivalent to x^y. With three arguments, equivalent to (x^y) % z,


# Example
y = pow(5, 2)
print(y)



# যখন pow(5, 2, 5) এর মদ্যে ৩ arguments থাকবে ১ম দুইটি গুন হবে এবং পরেরটি সাথে ভাগ হবে ।
x = pow(5, 2, 5)
print(x)
print('\n')


# Example of abs
# Absolute Value
x = abs(-3)
print('Absolute Value of -3 :', x)
print("\n")


# Example
my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print("my_taxes : ", my_taxes)

print("\n")



# Problem Solve

# 1. Why doesn't 0.1+0.2-0.3 equal 0.0 ?

# Solve

x = 0.1 + 0.2 - 0.3
print("x", x)
print("\n")


# Which one of these is a floating point number?
"""
A: 3.2
B: 4
C: 500
D: 270000
E: 6
"""

# Solve
x = 3.2
print("floating point number : ", x)
print(type(x))
print("\n")

# Which of these will output the result 36?
"""
A: 30+*6
B: 6^6
C: 6**6
D: 6*6
E: 6+6+6+6+6
"""

# Solve
x = 6 * 6
print("output the result : ", x)
print('\n')

# In Python 3, what is the output of 1/2 ?
"""
A: 1
B: 0
C: 0.5
"""

# Solve
x = 1 / 2
print("output of 1/2 : ", x)

# Task:
# 100.25 -- Multiplication, division, exponent, addition, substraction, that equal to 100.25

# 10*10.10**2+100.25-1



