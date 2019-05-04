
"""
    Python Basic Syntax
"""

# Using Python Shell

"""
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world !")
Hello world !
>>>

"""

# Let us write a simple Python program in a script.

"""
C:\\Users\\Jibon Ahmed\\Desktop\\Python-Programming>python test.py
Hello world !

"""

# Python Identifiers

"""

A Python identifier is a name used to identify a variable, function, class, module or other object.
An identifier starts with a letter A to Z or a to z or an underscore(_) followed by zero
or more letters, underscores and digits(0 to 9).

"""


# Python does not allow punctuation characters such as @, $, and % within identifiers.

# Python is a case sensitive programming language.

# Here are naming conventions for Python identifiers

"""
1. Class names start with an uppercase letter. and All other identifiers start with a lowercase letter.

2. Starting an identifier with a single leading underscore indicates that the identifier is private.

3. Starting an identifier with two leading underscores indicates a strongly private identifier.

"""


'''
Reserved Words
These are reserved words and you cannot use them as constant or variable
or any other identifier names.

'''

# Example of Python keywords.

"""
and         exec        not
assert      finally     or
break       for         pass
class       from        print
continue    global      raise
def         if          return
del         import      try
elif        in          while
else        is          with
except      lambda      yield
"""

# Lines and Indentation

# Example

if 5 > 2:
    print("Five is greater then two")

"""
Python provides no braces to indicate blocks of code for class and function definitions or flow control.

Example:

>> > if True:
   print("True")
else:
   print("False")

"""


# Multi-Line Statements

# line continuation character (\)


a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9 + 10 + \
    11 + 12 + 13 + 14

print('Multiple line Sum : ', a)
print('\n')

# Statements contained within the [], {}, or () brackets
# do not need to use the line continuation character.

# Example

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(days)
print('\n')


# Quotation in Python

"""
Python accepts single ('), double (") and triple (''' or """ """)
quotes to denote string literals
"""


# Example
x = 'Hello world'
print(x)

y = "Welcome to python"
print(y)

z = "Quotation in Python"
print(z)
print('\n')


# Comments in Python
# sign is a comments

"""

Python Multi-line Comments

.....
.....
.....

"""


# Using Blank Lines
# Here, "\n" is used to create two new lines

print("Hello world !")
print('\n')


# Multiple Statements on a Single Line
# Example

"""
>>> import math; x = math.pi; print(x)
3.141592653589793
>>> 
"""
