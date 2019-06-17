
# Start :- 12:04 PM 6/12/2019

# Python Tuples

"""
Tuples ও list এর মত কাজ করে ।
tuple এর ভালু পরিবর্তন করা যায় না ।
tuple () কে দ্বারা এবং ভালুগুলো কে , দ্বারা আলাদা করতে হবে ।
tuple কোন ভালু অ্যাড ও করা যায় না ।
"""


# Tuples

"""
    1. Constructing tuples
    2. Basic tuples
    3. tuples immutability
    4. When to used tuples
"""


# Example of how to declare a tuple in python
print('How to declare a tuple :\n')


t1 = (1, 3, 5)
print('tuple  :', t1)
print(type(t1))


t2 = tuple('A')
print('tuple  :', t2)
print(type(t2))


t = 1, 2, 3, 4, 5
print("tuple  : ", t)
print(type(t))

print('\n')


# Example

myTuple = ('date', 'month', 'year')
print("tuple :", myTuple)


# Example

roles = ("Admin", "Operator", "User")
print('tuple :', roles)
print('\n')


# Example tuple multiple value assign
print('tuple multiple value assign :\n')


a, b, *c, d = ("Hello", 'there', (1, 3, 5, 6), 'world')
print('a  :', a)
print('b  :', b)
print('*c :', c)
print('d  :', d)
print('\n')


# tuple indexing and slicing
print('tuple indexing and slicing :\n')


# Access an item

my_tuple = ('one', 2, 3, 4, 5, 6, 'Seven', 8, 9, 10, 'end', True)

print('All tuple list   :', my_tuple)       # Print all tuple
print('all tuple list   :', my_tuple[:])    # Print all tuple
print('Length of tuple  :', len(my_tuple))  # Length of the tuple
print('first index      :', my_tuple[0])    # First index value
print('last index       :', my_tuple[-1])   # last index value
print('1st to 3th index :', my_tuple[0:3])  # 1st to 3 index value
print('2nd to 5th index :', my_tuple[2:5])  # 2nd to 5 index value
print('6th to all index :', my_tuple[6:])   # 6th index এর পর সব গুলো পাবো ।
print('Skipping 2 index :', my_tuple[::2])  # ২ ওয়ার্ড পর পর value গুলো পাবো । For Skipping 2 index each time
print('Reverse word     :', my_tuple[::-1])  # উল্টে দিক থেকে সবগুলো ভালু পাবো ।
print('Skipping 2 index :', my_tuple[0:17:2])   # For Skipping 2 index each time start 0 end 27
print('\n')


# Example of how to access tuple  element
print('tuple access item in tuple :\n')


per = (("Admin", "Operator", "Customer"), ("Developer", "Tester"), [1, 2], {"Stage": "Development, Python"})

print('permissions         :', per)
print("Length of tuple     :", len(per))
print('1st index 2nd index :', per[0][1])
print('2nd index 2nd index :', per[1][0])
print('3th index value     :', per[3]['Stage'])
print('\n')


# tuple unpacking
# tuple unpacking এর কাজ হোল tuple এর মধ্যে যেকোনো variable এর মান change করে ।

print('tuple unpacking :\n')

numbers = (1, 2, 3)
a, b, c = numbers   # Here a, b, c is a variable
print(a)
print(b)
print(c)
print('\n')


# tuples immutability
print('tuples immutability :\n')

tryTuple = (6, 9, 4)
print(tryTuple)

"""
x = tryTuple[0] = (10)
print(x)

'''
class 'tuple'>
    x = tryTuple[0] = (10)
TypeError: 'tuple' object does not support item assignment
tuple এর মান change করা যায় না ।
'''
"""
print('\n')


# Basic tuple Method
print('Tuple Method :\n')


tuple_method = [1, 3, 5, 3]
print('tuple method  :', tuple_method)

tuple_method.append(7)                 # append() we can add one item at a time
print("append tuple  :", tuple_method)

tuple_method.extend(['one', 'two'])    # extend() we can add multiple item
print("extend tuple  :", tuple_method)

tuple_method.remove('two')             # remove elements from a list
print('Remove tuple  :', tuple_method)

tuple_method.reverse()                 # reverse() সবগুলো উল্টো দিকথেকে print করবে ।
print('reverse tuple :', tuple_method)

print("\n")


# End :- 1:18 PM 6/12/2019


