
# Print Formatting in python

"""
    String Formatting
"""


"""
Rules: string formatting ব্যবহার করলে আমদেরকে "%s" %(variable name) দিতে হবে ।
"""
print("\n")


# Example:

print("String formatting :- ")

s = "String formatting"
print("Learn : %s" % (s))
print('\n')


# Example
s = 'string'
print('place my variable here : %s' % (s))  # %(s)) হোল object variable label
print('\n')


# Example
x = 124
print('place my variable here : %s' % (x))
print('\n')


# Example
x = 13.13
print('place my variable here : %s' % (x))
print('\n')


# Floating point Formatting

"""
Rules: Floating Formatting ব্যবহার করলে আমদেরকে "%f" %(variable name) দিতে হবে ।
"""


# Example

print("Floating Formatting :- ")

x = 12345.0000000
print("My Number is : %f" % (x))
print('\n')


# Example
x = 13.133
print('place my variable here : %1.1f' % (x))
#  %1.1f' %(x)) এইখানে %1. হোল দশমিক এর আগের মান আর .1f কয়ঘর প্রজন্ত মান নিতে পারি
print('\n')


# Example
x = 13.133
print('place my variable here : %10.1f' % (x))
print('\n')


# Example
x = 13.133
print('place my variable here : %1.10f' % (x))
print('\n')

# More Example

print('Floating point numbers: %1.2f' %(4569.456144))

print('Floating point numbers: %1.0f' %(4579.00345))

print('Floating point numbers: %10.2f' %(1263.6400))

print('Floating point numbers: %10.5f' %(13.14))
print('\n')


# Multiple Formatting Method

print("Multiple Formatting Method :-")

print('First : %s, Second : %s, third : %s' % ("We", "Love", "Bangladesh"))
print('\n')


# Example
print('First : {x} second : {y} third : {x}'.format(x="Hello", y=69))
print('\n')


# Example
print("One : {x} two : {y} three : {z}".format(x=1, y=2, z=3))
print('\n')


# Example

message = " if x = {x} and y = {y}, then x+y = {z}".format(x=7, y=5, z=7+4)
print(message)
print('\n')


# Converting to String

print("Converting to String :- ")

# %s str() method
print("converting to string %s" % (124))
print('\n')

# or %r repr() Function
print("converting to string %r" % (124))
print('\n')


"""
Output formatting in python ?
"""

# Example

a = input("Enter anything : ")

print(a, end='')    # output গুলো পাশাপাশি show করবে ।

print('\n')
input("Press < Enter : ")

