
# String

"""
String : A string is a sequence of characters.

একগুচ্ছ ক্যারেক্টার বা কিছু ওয়ার্ডের সিকুয়েন্সকে সাধারণত স্ট্রিং বলা হয়ে থাকে।
"""

# Rules of String

""" 
>>> # কিছু ক্যারেক্টারকে সরাসরি একটি স্ট্রিং এর মধ্যে ব্যবহার করা যায় না।
>>> ' I don't like this '
SyntaxError: invalid syntax
>>>
>>> ' I I don't\' t Like this '
" I I don' t Like this "
>>>


"""

# How to learn String

"""
1. Creating String
2. Printing string
3. String indexing and slicing
4. String Properties
5. String Method
6. String formatting

"""

# How to create a string in Python?

# to create string in python you need to use ' ' or " " or """ """

# Example

# single string

my_string = 'Hello'
print(my_string)



# Entire Phrases
my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


# Problem of single ''
'''
z = 'I' am a string '
print(z)
'''

# Example
z = "I'm a string "
print(z)


# Example
x = ' "This is a quote" '
print(x)

# \n new line
print('hi there\n how are you')


# \t tab means 5 space
print('hi there\t how are you')


# we can also use a function called len() to check the length of string
x = "Hello World"
x = len(x)
print(x)
# print(len(x))


# How to access characters in a string? Or String indexing

x = "Hello World"
print(x)
y = x[1]
print("1 : ", y)


# Negative indexing

y = x[-1]
print("-1 : ", y)


# String slicing

x = "Hello World"
print(x)
y = x[1:]
print("1:", y)


# print all string
y = x[::]
print("::", y)

# or

y = x[:]
print(":", y)


# print 1 index to 4 index value
y = x[1:4]
print(y)


# print all string
y = x[:-1]
print(y)


# এইখানে আমারা ::2 ব্যহহার করছি । ঃঃ হোল সব স্ট্রিং আর 2 হোল step size
# index এর position 2 করে পর পর print করবে ।

y = x[::2]
print(y)


# Example
y = x[::-1]
print(y)

# Now Example of string

x = "Welcome to python 3"
print(x)

# How to print --> output : w3

y = x[0 ] +[-1]
print(y)


# String Properties

'''
x = "Hello world"
x[0] = "Y"
print(x)

TypeError: 'str' object does not support item assignment

'''
# value add করতে পারি এইভাবে ।

x = "Hello world"
x = x + " concatenate me !"
print(x)


# আমারা এখন letter গুণ করবো

letter = 'Z'
x = letter * 10
print(x)


# String Method

# আমরা কিভাবে String এর সব Method পাবো ।
# cmd -->python --> help() --> str --> Enter
# upper() এর কাজ হোল সব letter গুলো বড় হবে ।

s = "Hello World"
x = s.upper()
print(x)

# সবগুলো letter lower হবে ।
x = s.lower()
print(x)

# split('e') দ্বারা আমি e কে remove করলাম ।
x = s.split('e')
print(x)
# output : ['H', 'llo World']


# Example

a = ' I Love Python '
print(a)
print(type(a))
print('\n')


# Example

# ইনপুট দেয়ার সময় ডাবল বা সিঙ্গেল কোটেশন যাই ব্যবহার করা হোক না কেন, আউটপুটের সময় সিঙ্গেল কোট দিয়ে সেই স্ট্রিং কে দেখায়।
b = " I Love Django "
print(b)
print('\n')


# Example 3 আমরা নাম্বার এন্ড স্ট্রিং কে একসাথে যোগ করবো

a = 7
b = " Jibon "
a = str(7)
print("A + B : ", a + b)
print('\n')

for i in range(1, 10):
    print(i)


# Now More Example of string


# Example of capitalize() শুধু প্রথম  litter টি বড় হবে বাকী সব গুলো ছোট হবে ।
x = "welcome To Python"
y = x.capitalize()
print(y)
print('\n')


# Example of casefold() এই  function এর কাজ হোল সবগুলো litter কে ছোট করে দিবে ।

"""
>>> x = "WELCOME TO PYTHON 3"
>>> y = x.casefold()
>>> y
'welcome to python 3'
>>>

"""

# example

"""
>>> x = "Jayed Hossain"
>>> x
'Jayed Hossain'
>>> y = x.replace('Jayed', "Jibon")
>>> y
'Jibon Hossain'
>>>
"""


# Escape Sequence in Python

"""
\newline	Backslash and newline ignored
\\	        Backslash
\'	        Single quote
\"	        Double quote
\a	        ASCII Bell

\b	        ASCII Backspace
\f	        ASCII Formfeed
\n	        ASCII Linefeed
\r	        ASCII Carriage Return
\t	        ASCII Horizontal Tab
\v	        ASCII Vertical Tab
\ooo	    Character with octal value ooo
\\xHH	    Character with hexadecimal value HH
"""


'''
4- String Operation
'''

'''
ইন্টিজার বা ফ্লটের মত, স্ট্রিংকেও যোগ করা যায় যাকে কনক্যাটেনেশন বলা হয়।
'''

print("Python" + " Django")

print('2' + '2')

print(2*2)

'''
নন স্ট্রিং ডাটার সাথে স্ট্রিং টাইপের ডাটাকে যুক্ত করে সুন্দর স্ট্রিং আউটপুট তৈরি করতে format মেথড ব্যবহার করা হয়।

'''

skill = "My Skills on Bootstrap: {0}, Python: {1}, Java: {2}, Django: {3}". format(7, 6.5, 5, 8)
print(skill)


x = '{2}, {1}, {0}'.format('Python', 'Django', 'Html')
print(x)


y = '{0}{1}{0}'.format('PHp', 'Sql')
print(y)


message = "If x = {x} and y = {y}, then x+y = {z}".format(x=20, y=30, z=20+30)
print(message)


'''
কিছু গুরুত্বপূর্ণ ফাংশন .. আমারা IDLE বা Cmd তে গিয়ে help() তারপর str দিলে সব দেখতে পাব স্ট্রিং এর object গুলো

'''

a = 'Jayed Ahmed'

b = a.replace('Jayed','Jibon ')
print(b)

c = 'Jui Ahmed'

x = c.startswith('A')
print(x)


a = 'jayed hossain jibon'

x = a.capitalize()
print(x)

# x = a.swapcase()
# print(x)

x = a.title()
print(x)

x = a.rindex('n')
print(x)

y = a.find('o')
print(y)
