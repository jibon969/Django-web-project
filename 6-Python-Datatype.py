
"""
    Python Data Types
"""


# Python has five standard data types −

"""
Numbers
String
List
Tuple
Dictionary
"""


# Python Numbers
# Number data types store numeric values.

print("Number : ")
x = 34
print(x)
print("\n")


# Python supports four different numerical types

"""
int (signed integers) long (long integers, they can also be represented in octal and hexadecimal)
float (floating point real values) complex (complex numbers)
"""


# Example of integers

print("Integers number :- ")
a = 5
print(a)
print("Data type: ", type(a))
print("\n")


# floating point numbers

print("Floating point numbers :- ")
x = 7.0
print(x)
print(type(x))
print("\n")


# Example Complex numbers

print("Complex Numbers :- ")
y = 7 + 6j
print(y)
print("real number       : ", y.real)
print("imaginary number  : ", y.imag)
print("\n")


# Hexadecimal

print("Hexadecimal :- ")
x = hex(246)
print("Hexadecimal of x :", x)


# Using the function bin() you can convert numbers into their binary format.

x = bin(1234)
print("Binary of 1234 :", x)
print('\n')


# String
# String are set of characters represented in the quotation marks


print("String :- ")
str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string
print('\n')


# Python Lists

"""
 A list contains items separated by commas and 
 enclosed within square brackets ([]).
 """


print("Python List :- ")
list = ['abcd', 786, 2.23, 'Jayed', 70.2]

another_list = [123, 'Hossain']

print(list)                 # Prints complete list
print(list[0])              # Prints first element of the list
print(list[1:3])            # Prints elements starting from 2nd till 3rd
print(list[2:])             # Prints elements starting from 3rd element
print(another_list * 2)     # Prints list two times
print(list + another_list)  # Prints concatenated lists

# We can Update list
x = list[0] = "New item"
print("add new item list : ", x)

print('\n')


# Python Tuples


print("Python Tuples :- ")
tup = ('abcd', 786, 2.23, 'Jayed', 70.2)
another_tup = (123, 'Hossain')

print(tup)                 # Prints complete list
print(type(tup))           # Print Data type
print(tup[0])              # Prints first element of the Tuples
print(tup[1:3])            # Prints elements starting from 2nd till 3rd
print(tup[2:])             # Prints elements starting from 3rd element
print(another_tup * 2)     # Prints Tuples two times
print(tup + another_tup)   # Prints concatenated Tuples
print('\n')


# Tuples can not updated

"""
>>> tup[0] = "New"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tup[0] = "New"
TypeError: 'tuple' object does not support item assignment
>>> 
"""

# Python Dictionary

"""
Dictionaries are enclosed by curly braces ({ }) 
and values can be assigned and accessed using square braces ([]).
"""


# Example


print("Python Dictionary :- ")
dict = {}

dict['one'] = "This is one"
dict[2] = "This is two"

list = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(dict['one'])          # Prints value for 'one' key
print(dict[2])              # Prints value for 2 key
print(list)                 # Prints complete dictionary
print(list.keys())          # Prints all the keys
print(list.values())        # Prints all the values
print('\n')


# Data Type Conversion
# এক টাইপ থেকে অন্য টাইপ এ কনভার্ট করা বুঝায়। একে টাইপ কাস্টিং ও বলা হয়ে থাকে।


""""
Example of  String to Integer Conversion
"""

print("Type Conversion :- ")

x = "123"
y = int(x)
print("String to integer : ", y)
print('\n')


"""
Example of float to Integer Conversion
"""

i = 12.69
print(i)
j = int(i)
print("float to Integer Conversion : ", j)
print('\n')


"""
Example of String to float Conversion
"""

x = "123.456"
print(x)
y = float(x)
print("String to float Conversion : ", y)
print('\n')


"""
Example of Integer to float Conversion
"""

a = 123
print(a)
b = float(a)
print("Integer to float Conversion : ", b)
print('\n')


# Learn More

"""
int(x [,base])
Converts x to an integer. base specifies the base if x is a string.


long(x [,base] )
Converts x to a long integer. base specifies the base if x is a string.


float(x)
Converts x to a floating-point number.


complex(real [,imag])
Creates a complex number.


str(x)
Converts object x to a string representation.


repr(x)
Converts object x to an expression string.


eval(str)
Evaluates a string and returns an object.


tuple(s)
Converts s to a tuple.


list(s)
Converts s to a list.


set(s)
Converts s to a set.


dict(d)
Creates a dictionary. d must be a sequence of (key,value) tuples.


frozenset(s)
Converts s to a frozen set.


chr(x)
Converts an integer to a character.


unichr(x)
Converts an integer to a Unicode character.


ord(x)
Converts a single character to its integer value.

hex(x)
Converts an integer to a hexadecimal string.

oct(x)
Converts an integer to an octal string.

"""
