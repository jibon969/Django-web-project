# Start :-  1:38 PM 6/10/2019

# Python Number System


# পাইথনের কনসোলে সহজেই ম্যাথেম্যাটিক্যাল ক্যালকুলেশন করা যায়। ( Basic Operations + , - , * , % )

"""
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2 + 4
6
"""

print("Basic Operations : \n")

# Example of Addition
x = 2 + 4
print('Addition = ', x)

# Example of Subtraction
x = 2 - 4
print('Subtraction = ', x)


# Example of Multiplication
x = 2 * 4
print('Multiplication = ', x)


# Example of Division
x = 6 / 2
print('Division = ', x)


# Example of Remainder
x = 6 % 2
print('Remainder = ', x)
print('\n')


# যোগ বিয়োগের মতই গুন ভাগের কাজও এখানে সহজেই করা যায়।

x = (2 + 2 / 3 - 4)
print(x)


# Example
x = 50 - (3 + 3 * 2)
print(x)


#  নাম্বারের আগে মাইনাস (-) সাইন দিয়ে নেগেটিভ নাম্বার নির্ধারণ করে দেয়া হয়।

x = -9 + 2
print("Negative int x : ", x)
print('\n')


# Example

""" 
>>> # সাধারণ গণিতের মতই পাইথনে কোন সংখ্যাকে শূন্য দিয়ে ভাগ করতে গেলে এরর আসবে
>>> 45/0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    45/0
ZeroDivisionError: division by zero
"""


# Example of Exponentiation or power

"""
যোগ, বিয়োগ, গুন ভাগ বাদেও পাইথনে Exponentiation or power এর সাপোর্ট আছে 
যাকে আমরা একটি সংখ্যার উপর আরেকটা সংখ্যার পাওয়ার বলে থাকি।
"""


# Example

x = 2**3
print("Power of x :", x)
print('\n')


# floor division ভাগশেষ নির্ণয়ের জন্য ব্যবহার করা হয়।

x = 10 // 3
print("floor division of x : ", x)
print('\n')


# Example of tax calculate

print("tax calculate : \n")

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print("my_taxes : ", my_taxes)
print("\n")


# Example of math function

#  pow() With two arguments, equivalent to x^y. With three arguments, equivalent to (x^y) % z,

y = pow(5, 2)
print(y)


# যখন pow(5, 2, 5) এর মদ্যে ৩ arguments থাকবে ১ম দুইটি গুন হবে এবং পরেরটি সাথে ভাগ হবে ।
x = pow(5, 2, 5)
print(x)
print('\n')


# Example of abs

x = abs(-3)
print('Absolute Value of -3 :', x)
print("\n")


# Now Example of math import

import math
x = math.sqrt(81)
print("sqrt : ", x)
print("\n")


# Example
y = math.floor(23.76)
print("floor : ", y)
print("\n")


# Example
a = math.degrees(1317.8029288008934)
print("degrees : ", a)
print("\n")


# Example of log10
b = math.log10(12)
print("log10(12)", b)
print("\n")


# Example of factorial
d = math.factorial(6)
print("factorial : ", d)
print("\n")


# Example of cos
e = math.cos(90)
print("cos(90) : ", e)
print("\n")


# Python Decimal
x = (1.1 + 2.2) == 3.3
print(x)

y = 1.1 + 2.2
print(y)
print("\n")

# Decimal

print("Decimal Number : \n")

from decimal import Decimal as D  # here D is variable

print('decimal + =', D('1.1') + D('2.2'))
print('decimal * =', D('1.2') * D('2.50'))
print("\n")


# Example of math function

print('pi = ', math.pi)
print('cos =', math.cos(math.pi))
print('exp =', math.exp(10))
print('log10 =', math.log10(1000))
print('sing =', math.sinh(90))
print('factorial =', math.factorial(5))
print("\n")

# Why doesn't 0.1+0.2-0.3 equal 0.0 ?

x = 0.1 + 0.2 - 0.3
print("x", x)
print("\n")


# Example of random

import random

print("Random Number : ", random.randrange(10, 20))
x = ['a', 'b', 'c', 'd', 'e', 'random', 'math']
print("Random Choice : ", random.choice(x))
print('\n')
