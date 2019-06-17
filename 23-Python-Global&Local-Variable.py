
# Start : 8:38 PM 6/13/2019


# scope :-

""""
    Function এর ভিতরের  variable -- > Local
    Function এর বাইরের  variable  -- > Global
"""


# Example

a = 10  # global variable


def somethong():

    a = 15 # local variable
    print(a)


print(a)

somethong()

print('\n')


# Example


a = 10


def do_something():
    global a
    a = 15
    print('Inside the function', a)


somethong()
print('Outside of function', a)
print('\n')


# Function using for global and local variable

a = 23
print(id(a))


def hello_something():
    a = 9
    x = globals()['a']
    print(id(x))
    print('inside the function', a)
    globals()['a'] = 15


hello_something()


# End :- 11:16 PM 6/13/2019


