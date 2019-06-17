
# Start :- 9:22 PM 6/16/2019

# Constructor in Inheritance

"""
    1. Constructor in Inheritance
    2. Method Resolution Order (MRO)
"""


# Example

class A:

    def __init__(self):
        print('in A init')

    def feature(self):
        print('Feature 1 is working')


class B(A):

    def __init__(self):
        super().__init__()   #
        print('in B init')

    def feature2(self):
        print('Feature 1 is working')


a1 = B()

print('\n')


# Example

class X:

    def __init__(self):
        print('in A class')

    def hello(self):
        print('Hi, there')


class Y:

    def __init__(self):
        print('in B init')

    def show(self):
        print('Hello World !')


class Z(X, Y):

    def __init__(self):
        super().__init__()
        print('in Z init')

    def feat(self):
        super().hello()


z = Z()
z.hello()

print('\n')

