# Start :- 5:35 PM 6/10/2019

# Print Formatting in python

"""
    1. Output formatting
    2. String Formatting
    3. Floating point Formatting
"""


# Example of Output formatting

print("Hello World !")

print('Hello \n World !')

print("Hello", end=' ')   # output গুলো পাশাপাশি show করবে ।

print('\n')


# Example of string formatting

# string formatting ব্যবহার করলে আমদেরকে "%s" %(variable name) দিতে হবে।
print("String formatting :- ")

s = "String formatting"
print("Learn python %s" % (s))


# Example
s = 'string'
print('place my variable here : %s' % (s))  # %(s)) হোল object variable label


# Example
a = 69
print('My number is %s' %(a))

# Example

b = "jayed.swe@gmail.com"
print("My email address %s" %(b))
print('\n')


# Multiple Formatting Method

print("Multiple string Formatting Method \n")

print('First : %s, Second : %s, third : %s' % ("We", "Love", "Bangladesh"))


# Example
print('First : {x} second : {y} third : {x}'.format(x="Hello", y=69))


# Example
print("One : {x} two : {y} three : {z}".format(x=1, y=2, z=3))


# Example
message = "if x = {x} and y = {y}, then x+y = {z}".format(x=7, y=5, z=7+4)
print(message)
print('\n')


# Converting to String
print("Converting to String :- ")

# %s str() method
print("converting to string %s" % (124))


# or %r repr() Function
print("converting to string %r" % (124))
print('\n')


# Floating point Formatting
# Floating Formatting ব্যবহার করলে আমদেরকে "%f" %(variable name) দিতে হবে ।
print("Floating Formatting \n")


x = 12345.0000000
print("My Number is : %f" % (x))


# Example
x = 13.133
print('place my variable here : %1.1f' % (x))
#  %1.1f' %(x)) এইখানে %1. হোল দশমিক এর আগের মান আর .1f কয়ঘর প্রজন্ত মান নিতে পারি


# Example
x = 13.133
print('place my variable here : %10.1f' % (x))


# Example
x = 13.133
print('place my variable here : %1.10f' % (x))
print('\n')

# More Example
print('Floating point numbers: %1.2f' %(4569.456144))
print('Floating point numbers: %1.0f' %(4579.00345))
print('Floating point numbers: %10.2f' %(1263.6400))  # আগে ১০ টি space নিয়ে নিবে ।
print('Floating point numbers: %10.5f' %(13.14))
print('\n')


# 5 + 6 = 11

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = a + b

print(a, '+', b, '=', c)
print('{} + {} = {}'.format(a, b, c))
