
# Start :  2:13 PM 6/16/2019

# Constructor, Self and Comparing Objects

"""
    Every time you create an object it is allocated to new space
    Size of an object :- depend on the variables who allocates size to object.
"""


# Example

class Computer:
    pass


c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))
print('\n')


# Example

class MyComputer:
    def __init__(self):
        self.name = 'jui'
        self.age = 25


com1 = MyComputer()
com2 = MyComputer()

print(com1.name)
print(com2.name)
print('\n')


# if i change name value
com1.name = 'Jayed'

print(com1.name)
print(com2.name)
print('\n')


# Example

class Person:
    def __init__(self):
        self.name = 'hello'
        self.age = 23

    def update(self):
        self.name = 'July'


# Object Creation

x = Person()
y = Person()

print('Name :', x.name)
print('Age  :', y.age)
print('\n')

# update from self.name = 'hello'
x.name = 'Jibon'
print('Name :', x.name)


# calling update function
x.update()
print('Called update function :', x.name)



