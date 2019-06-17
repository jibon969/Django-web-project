
# Start :- 8:26 PM 6/11/2019


"""
1. Creating List
2. Nesting list
3. How to access elements from a list.
4. indexing and slicing List
5. Basic list Method
6. Built-in Functions with List
"""

"""
    list এ আমার বিভিন্ন ধরনের ডাটা রাখাতে পারি । 
    লিস্ট এর ভেলু কে পাওয়ার জন্য আমারা index কে call করতে হবে । 
    আর index শুরু হয় [0] and  [-1]
"""


# Creating List
print('How to Creating List :\n')

a = list()
b = []
c = [1, 2, "List", 1.5, ]

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))
print('\n')


# Example of nested list
print("Nested list :\n")


my_list = ["python", [8, 4, 6], ['a']]
print(my_list)
print('\n')

# How to access elements from a list.

"""
    We can use the index operator [] to access an item in a list. 
    Positive indexing start from  :   0
    Negative indexing  start from : - 1
"""
print('How to access elements from a list :\n')


my_list = [1, 2, 3, 'hello', 6.7, 'world']

print('all index   :', my_list)
print('first index : ', my_list[0])
print('2nd index   :', my_list[2])
print('4th index   :', my_list[4])
print('Negative last index  :', my_list[-1])
print("\n")


# Nested List to access element
print("Nested List to access element :\n")

true = 'This is true'
d = [1, 2, 3, 4, ['hello', 'world', 6.9, 5, True], True, true]

print('all list             :', d)         # all list
print('1st index            :', d[1])      # 1st index
print('4th index            :', d[4])      # 4th index
print('4th index 2nd index  :', d[4][2])   # 4th index 2nd index  nested list
print('4th index 4th index  :', d[4][4])   # 4th index 4th index  nested list
print("\n")


# List indexing and slicing
print('list indexing and slicing :\n')


list1 = ['one', 2, 3, 4, 5, 6, 'Seven', 8, 9, 10, 'end', True]

print('All list         :', list1)       # Print all list
print('all list         :', list1[:])    # Print all list
print('Length list      :', len(list1))  # Length of the list
print('first index      :', list1[0])    # First index value
print('last index       :', list1[-1])   # last index value
print('1st to 3 index   :', list1[0:3])  # 1st to 3 index value
print('2nd to 5 index   :', list1[2:5])  # 2nd to 5 index value
print('6th to all index :', list1[6:])   # 6th index এর পর সব গুলো পাবো ।
print('Skipping 2 index :', list1[::2])  # ২ ওয়ার্ড পর পর value গুলো পাবো । For Skipping 2 index each time
print('Reverse word     :', list1[::-1])  # উল্টে দিক থেকে সবগুলো ভালু পাবো ।
print('Skipping 2 index :', list1[0:17:2])   # For Skipping 2 index each time start 0 end 27
print('\n')


# How to change or add elements to a list ?
print("change or add elements to a list :\n")


even = [2, 4, 6, 8, 10]
print(even)


even[4] = 14    # change 4 and replace 14
print("change element :", even)


# change 2nd to 4th items
even[1:4] = [3, 5, 7]
print("change element :", even)
print("\n")


# Example

c = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], True, true]

c[1] = ['Jibon', '12', 13]

print(c[3], c[1][1])
print(str(c[3])+c[1][1])
print(str(c[3])+" "+c[1][1])
print('\n')


# Basic list Method
print('Basic list Method :\n')

list2 = [1, 3, 5, 3]

list2.append(7)                 # append() we can add one item at a time
print("append    :", list2)

list2.extend(['one', 'two'])    # extend() we can add multiple item
print("extend    :", list2)

list2.remove('two')             # remove elements from a list
print('Remove    :', list2)

list2.reverse()                 # reverse() সবগুলো উল্টো দিকথেকে print করবে ।
print('reverse   :', list2)

print("\n")


# List matrix
print('list matrix :\n')
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]
print(matrix)

x = matrix[0]
print(x)

# print first list last value
x = matrix[0][2]
print(x)
print('\n')


# Built-in Functions with List

'''
Function	    Description
all()	        Return True if all elements of the list are true (or if the list is empty).
any()	        Return True if any element of the list is true. If the list is empty, return False.
enumerate()	    Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	        Return the length (the number of items) in the list.
list()	        Convert an iterable (tuple, string, set, dictionary) to a list.
max()	        Return the largest item in the list.
min()	        Return the smallest item in the list
sorted()	    Return a new sorted list (does not sort the list itself).
sum()	        Return the sum of all elements in the list.
'''

# End :- 10:35 PM 6/11/2019

