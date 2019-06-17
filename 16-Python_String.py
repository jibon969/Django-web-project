
# Start :- 2:48 PM 6/11/2019

# Python String


"""
    String : A string is a sequence of characters.
    একগুচ্ছ ক্যারেক্টার বা কিছু ওয়ার্ডের সিকুয়েন্সকে সাধারণত স্ট্রিং বলা হয়ে থাকে।
"""


# String Table of Contents

"""
    1. Creating String
    2. Printing string
    3. String indexing and slicing
    4. String Properties
    5. String Method
    6. String formatting
"""


# How to create a string ?

''' 
' ' 
or 

" " 
or 

""" """
'''


# Example of create a string
print('How to create a string :\n')

a = 'This is a string'
b = "This is a another string"
c = """I'm a string"""
print(a)
print(b)
print(c)
print(type(a))
print('\n')


# Built-in string functions
# go to idle --- and just help() then str


# Printing string
print('Printing string :\n')

my_str = 'Hello World !'
print(my_str)
print(type(my_str))
print('\n')


# String indexing and slicing
print('String indexing and slicing :\n')

"""
    String indexing and slicing are two type :-
    1. Positive indexing 
    2. Negative indexing
"""


# Example of Positive indexing

st = "Hello World !"
print(st)

new_st = st[0]
print('Positive index first value :', new_st)
print('\n')


# Example of Negative indexing

s = "learn string"
print(s)

new_s = s[-1]
print('Negative index last value :', new_s)
print('\n')


# More Example of String indexing and slicing

str1 = 'String indexing and slicing'
print('All String       :', str1)       # Print all string
print('all sting        :', str1[:])    # Print all string
print('Length string    :', len(str1))  # Length of the String
print('first index      :', str1[0])    # First index value
print('last index       :', str1[-1])   # last index value
print('1st to 3 index   :', str1[0:3])  # 1st to 3 index value
print('2nd to 5 index   :', str1[2:5])  # 2nd to 5 index value
print('6th to all index :', str1[6:])   # 6th index এর পর সব গুলো পাবো ।
print('Skipping 2 index :', str1[::2])  # ২ ওয়ার্ড পর পর value গুলো পাবো । For Skipping 2 index each time
print('Reverse word     :', str1[::-1])  # উল্টে দিক থেকে সবগুলো ভালু পাবো ।
print('Skipping 2 index :', str1[0:17:2])   # For Skipping 2 index each time start 0 end 27
print('\n')


# String Properties
print('String Properties :\n')

x = "Hello "
y = x + "Concatenation"  # string value add করতে পারি এইভাবে ।
print('add value :', y)


# Example of string addition

s = "Python String"
x = s[:4] + s[:4]
print('string addition :', x)


# Example of string multiplication

x = "letter "
print('Multiplication : ', x * 3)  # আমারা এখন letter গুণ করতে পারি
print('\n')


#  String Method

"""
    আমরা কিভাবে String এর সব Method পাবো ।
    cmd -->python --> help() --> str --> Enter
"""

print('String Method :\n')


n = "hi There s"
print(n)
print('upper        :', n.upper())
print('lower        :', n.lower())
print('split        :', n.split())
print('find         :', n.find('e'))
print('startswith   :', n.startswith('h'))
print('endswith     :', n.endswith('e'))
print('replace      :', n.replace('s', ''))
print('title        :', n.title())
print('index        :', n.index('T'))
print('capitalize   :', n.capitalize())
print('\n')


# String formatting
print('String formatting \n')

my_skills = "Html : {0}, CSS : {1}, Javascript: {3}, jQuery:{4}, Bootstrap: {5}, python:{6}".format(90, 84, 60, 69, 78, 78, 79)
print(my_skills)


# Example
s = 69
print('My number is : %s' %(s))


# Example
message = "If x = {x} and y = {y}, then x + y = {z}".format(x=20, y=30, z=20+30)
print(message)
print('\n')


# End :- 5:36 PM 6/11/2019
