
"""
    Lets Learn input Function
"""

x = input('Enter anything : ')
print(x)
print("\n")


# Print only integer number in python ?

x = int(input("Enter only integer number : "))
print(x)
print('\n')


# Print only Floating-point number in python ?

x = float(input("Enter your floating Point number  : "))
print(x)
print('\n')


# Now Example of eval

# eval এর কাজ হোল string কে যোগ করা ।
z = eval("2+3")
print("Eval means string addition : ", z)
print('\n')


# Example
a = "Welcome to python family"
print(a)
b = a.split(',')
print(b)
print('\n')


# How to use Split in Python
# split() এর কাজ হল প্রত্যেকটি sentence কে string আকারে list এর মদ্যে রাখবে ।

x = "How to learn Python"
c = x.split()
print(c)
print(type(c))
print('\n')


# More  Example

a = "As you can see from this code, the function splits our original string which includes three colors and then stores each variable in a separate string"

b = a.split()
print(b)
print("\n")
