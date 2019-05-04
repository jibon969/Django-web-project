"""
    Python Data Types
"""

# Example of Data type

"""
int, float, str, boolean, long, complex, unicode

Python has five standard data types :- 

Numbers, String, List, Tuple, Dictionary

"""
print("\n")


# Example of int
print("Example of int :")

a = 5
print(a)
print("Data type :- ", type(a))
print("\n")


# Example float

print("Example of float : ")

a = 7.5
print(a)
print("Data type :- ", type(a))
print("\n")


# Example of str

print("Example of str : ")

a = 'Welcome to python string'
print(a)
print("Data type :- ", type(a))
print("\n")

# Example of boolean
print("Example of boolean : ")

a = True
print(a)
print("Data type :- ", type(a))
print("\n")

# Example of long

print("Example of long : ")
x = 187687654564658970978909869576453
print(x)
print("Data type :- ", type(x))
print("\n")

# Example of complex

print("Example of complex : ")
x = 3 + 5j
print(x)
print("real number       : ", x.real)
print("imaginary number  : ", x.imag)
print("Data type :- ", type(x))
print("\n")


# Example of unicode

print("Example of unicode : ")
s = u"\U0001F4A9"
print(s)
print("Data type :- ", type(s))
print("\n")


print("Python has five standard data types : \n")

# Python Numbers
# Number data types store numeric values.

print("Number : ")
x = 34
print(x)
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

print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th
print(str[2:])       # Prints string starting from 3rd character
print(str * 2)       # Prints string two times
print(str + "TEST")  # Prints concatenated string
print('\n')


# Python Lists

"""
 A list contains items separated by commas and enclosed within square brackets ([]).
"""

print("Python List :- ")
list = ['one', 786, 2.23, 'two', 70.2]

another_list = [123, 'three']

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

