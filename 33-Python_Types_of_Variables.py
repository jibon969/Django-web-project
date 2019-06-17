
# Start :- 2:50 PM 6/16/2019

# Types of Variables

"""
    Variable :
    1. instance variable
    2. class (static) variable
"""


# Example

class Car:
    def __init__(self):
        self.mil = 10   # instance of object that means we can change it.
        self.com = "BMW"


c1 = Car()
c2 = Car()

# We can change the value
c1.mil = 8

print(c1.com, c1.mil)
print(c2.com, c2.mil)

print('\n')


# Namespace

"""
Name space is an area where you create and store object/variable
    1. class namespace
    2. object/instance namespace
"""


# Example of class variable

class MyCar:
    wheels = 4  # class variable or static variable

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


x = MyCar()
y = MyCar()


# change instance object
x.mil = 8


# যদি instance variable এর মান change করতে চাই তাহলে
MyCar.wheels = 7


print(x.com, x.mil, x.wheels)
print(y.com, y.mil, y.wheels)
print('\n')


