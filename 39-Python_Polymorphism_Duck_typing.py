
# Start :- 9:48 PM 6/16/2019

# Polymorphism

"""
    1. Polymorphism_Duck typing
    2. Polymorphism_Operator Overloading
    3. Polymorphism_Method Overloading
    4. Polymorphism_Method overriding
"""


# Example of Duck typing

class Pycharm:

    def execute(self):
        print('Compiling')


class MyEditor:

    def execute(self):
        print('Spell check')


class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
