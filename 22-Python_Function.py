# Start :- 5:07 PM 6/13/2019


# Computer program এ আমারা দুইটি term শুনতে পাওয়া যায় ।

"""
    1. WET :- write everything twice.
    2. DRY :- Do not repeat yourself.
"""

# Why Function ?

"""
    Function :- Function হোল organized and reusable unit code এর একটি blog.
    Function একটির বেশি data return করতে পারে না । 
    Function : 1. built-in and 2. user defined
    আর Function শেষ হবে return keyword দ্বারা । 
"""


# Basic Syntax of Function

"""
def Function_Name(parentheses/ Argument):

        Statement 1
        Statement 2
        return expression
        
# Called the function
Function_Name( )
"""


# Example of Function
print('How to write a Function :\n')


# Example of Function

def hello():
    print('Hi')


hello()


# Example
def print_my_name(myname):
    print('Given Name :', myname)
    return


print_my_name('Jayed Hossain')


# Example
def my_ame(myname):
    print(myname)
    return


variable1 = 'Hello'
variable2 = 'world'

print(variable1)
print(variable2)
print('\n')


# Function Argument
print('Function Argument :\n')


def add(a, b, c):
    return a + b + c


temp = add(2, 4, 5)
print('add :', temp)
print('\n')


# Example of show double

def show_double(x):
    print(x*2)


show_double(3)
show_double(200)
print('\n')


# Pass by value pass by reference
print('Pass by value pass by reference :\n')


def update(n):
    n = 8
    print('n :', n)


update(10)
print('\n')


# Example

def update_me(x):
    x = 12
    print('x :', x)


a = 10
update_me(a)
print('a :', a)
print('\n')


# Example

def update_now(x):
    print(id(x))
    x[1] = 25
    print(x)


x = [10, 20, 30, 40, 50]
print(id(x))
update_now(x)
print('x :', x)
print('\n')


# Functional parameter or argument
print('Functional parameter or argument :\n')

"""
    1. Requirement Argument
    2. Keyword Argument
    3. Default Argument
    4. Variable length Argument
"""


# Requirement Argument
print('Requirement Argument :- ')


''' 
def add_number(a, b, c):
    return a + b + c


# TypeError: add_number() missing 1 required positional argument: 'c'
temp = add_number(1, 3)     
print('Requirement Argument :', temp)

'''


# Example

def add_number(a, b, c):
    return a + b + c


temp = add_number(1, 3, 2)
print('Requirement Argument :', temp)
print('\n')


# Example of Keyword Argument
print('Keyword Argument :- ')


def my_keyword_argument(a, b, c):
    return a + b + c


temp = my_keyword_argument(a=7, b=6, c=4)   # keyword argument a=7, b=6, c=4
print('keyword_argument :', temp)


# Example

def person(name, age):
    print('Name :', name)
    print('Age  :', age)


person(name='Hello', age=36)
print('\n')


# Default Argument
print('Default Argument :-')


def my_default_argument(a, b=7):
    print('a                :', a)
    print('default argument :', b)


my_default_argument(2)


#  Example of override existing default value

def person_info(name, age=18):
    print('Name     :', name)
    print('default  :', age)


person_info('Jui', 23)  # override the default age
print('\n')


# Variable length Argument
# * argument দিয়ে আমারা tuple অকারে ভালু গুলো পাব ।
print('Variable length Argument :-')


def my_sum(a, *b):
    print('a  :', a)
    print('*b :', b)
    print(type(b))


my_sum(2, 3, 4, 5, 6)
print('\n')


# Example

def total_sum(a, *b):
    c = a
    for i in b:
        c = c + i
        print('total sum :', c)


total_sum(5, 1, 2, 3, 4)
print('\n')


# Example

def calculate(*b):
    c = 0
    for i in b:
        c = c + i
    print('Calculate sum :', c)


calculate(1, 4, 6, 7, 89, 82, 48, 45)


# Keyword Variable length Arguments
print('Keyword Variable length Arguments :- \n')


"""
** kwargs আমারা multiple নিতে পারবো । আর এই data গুলো dictionary হিসাবে থাকবে । 
"""


def personal_details(name, **other):
    print('name       :', name)
    print('other info :', other)
    print(type(other))


personal_details('Jibon', age=24, dept='Swe', roll=969)
print('\n')


# Mixed Argument
print('Mixed Argument :-')


def mixed_argument(a, *args, **kwargs):
    print('a        :', a)

    print('*args    :', args)
    print('type     :', type(args))

    print('**kwargs :', kwargs)
    print('type     :', type(kwargs))


mixed_argument('Hello', 7, 8, 9, id=69, address='dhaka')
print('\n')


# Example একটি Function return করতে পারবে multiple value.

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(23, 1)
print(result1)
print(result2)
print('\n')


# End :-  8:36 PM 6/13/2019





