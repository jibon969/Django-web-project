
# Start : 8:31 AM 6/16/2019

# _init_method in python

# Special

"""
special variables :- __name__
special method :- __init__
"""


# Example

# class Computer:
#
#     # যদি init ব্যবহার করি তাহলে called হবে automatically ।
#     def __init__(self):
#         print('In init')
#
#     # এই Method ব্যবহার করলে অবশ্যই call করতে হবে ।
#     def config(self):
#         print('i5 16gb 2TB')
#
#
# # Object Creation
# com1 = Computer()
#
#
# # Calling Method
# com1.config()


# More Example

class MyComputer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Configuration is ', self.cpu, self.ram)


x = MyComputer('i5', '16gb ram')
y = MyComputer('i7', '32gb ram')


x.config()
y.config()





