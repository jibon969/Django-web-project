
# Start : 7:22 AM 6/16/2019


# Object Oriented Programming in Python


"""
Python Support :-
    1. Functional Programming
    2. Object Oriented Programming
    3. Procedure Oriented Programming
"""


# Procedure : যখন software তৈরি করবো বিভিন্ন ছোট ছোট module হোল function.


# What object will have ?

"""
object will have two thing, every object will have certain attributes and every object will have certain behavior.

Attributes :
    1. Data
    2. Properties
Behavior :
    action গুলো আমার Behavior।
"""

# Object will need to define variable.

# Method

"""
Function in object-oriented programming are called as method.
Method কিছু না , আমারা যাকে Function নামে চিনিছি সে যখন ক্লাস এর মধ্যে থাকে তখন তাকে আমারা method বলি । 
"""


# Class & Object

"""
class :- class keyword ব্যবহার করে python class তৈরি করা হয়, একটি class এর মধ্যে আমারা বিভিন্ন method/function
বা attribute or property থাকতে পারে ।

class এর নাম বড় হাতের letter দিয়ে শুরু হয় । 
"""


# কিভাবে class define করবো ।

"""
class Computer:
    Attribute:- variables
    Behavior :- Method (Function)

    def config(self):
        print('i5, 16gb, 1TB')


# com হোল object
com = Computer()    # Constructor বলা হয় ।
print(com)
print(type(com))

"""


# Example

class Computer:

    def config(self):
        print('16gb, 2TB')


com = Computer()
Computer.config(com)





