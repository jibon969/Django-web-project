
# Start :- 7:36 PM 6/16/2019

# Inheritance

"""
    Inheritance :- হোল real life - parent & child
"""


# Example of single level inheritance

class A:

    # supper class or parent class
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')


class B(A):

    # sub class or child class
    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')


a1 = A()
a1.feature1()
a1.feature2()


# Called B class

b1 = B()
b1.feature3()

print('\n')


# Multi Level Inheritance


class X:

    def html(self):
        print('How to learn Html')

    def css3(self):
        print('How to learn css3')


class Y:

    def bootstrap(self):
        print('How to learn bootstrap')

    def javascript(self):
        print('How to learn javascript')


class Z(X, Y):

    def backend(self):
        print('How to learn backend')


# access from X class
x = X()
x.html()
print('\n')


# access from Y class
y = Y()
y.bootstrap()
y.javascript()
print('\n')


# access from Z class
z = Z()
z.html()
z.css3()
z.bootstrap()
z.javascript()
z.backend()



