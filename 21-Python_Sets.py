
# Start : 8:28 PM 6/12/2019

# Python Set

"""
1. set - list এবং  dictionary এর মতো একই ধরনের কাজ করে ।
2. set  কে { } দ্বারা প্রকাশ কারা হয় ।
3. একটি  set এর একই সদস্য বারবার থাকতে পারে না ।
4. set কে indexing করা যায় না ।
5. set এ  duplicate value থাকলে একটি value print হবে ।
"""


# Set Description

"""
A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
Python’s set class represents the mathematical notion of a set.
A set itself may be modified, but the elements contained in the set must be of an immutable type.
"""


# How to create a set?

print("How to create a set : \n ")

my_set = {1, 3, 5, 7, 9, 1}
print(my_set)
print(type(my_set))
print('\n')


# set of mixed data types

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
print("\n")


# How to add set value
print('How to add set value :\n')


mySet = {1, 3, 3, 5}
print('mySet :', mySet)


# add an element
mySet.add(2)
print("add an element : ", mySet)


# add multiple elements

mySet.update([2, 3, 4, 5])
print("add multiple elements : ", mySet)
print('\n')


# How to remove elements from a set
print("How to remove elements from a set : \n")


new_set = {1, 3, 3, 4, 5}
print('new_set        :', new_set)


# Remove element
new_set.remove(3)
print('remove element :', new_set)
print('\n')


# Python Set Operations
print('Set Operations :\n')


# Example of Union Operations
# Union of A and B is a set of all elements from both sets.


print('Union Operations : ')
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("union : ", A.union(B))
# or
print("union : ", A | B)
print('\n')


# Example of Intersection
# Intersection of A and B is a set of elements that are common in both sets.


print("Intersection : ")

# initialize A and B
X = {1, 2, 3, 4, 5, 9}
Y = {4, 5, 6, 7, 8, 9}


print("intersection : ", X.intersection(Y))
# Or
print("intersection : ", X & Y)
print('\n')


# Set Difference
"""
Difference of A and B (A - B) is a set of elements that are only in A but not in B. 
Similarly, B - A is a set of element in B but not in A.
যেই এলেমেন্ত গুলো same আছে ওই গুলি বাদ যাবে । 
"""

print("Set Difference : ")
# initialize A and B
A = {1, 2, 3, 4, 5, 7}
B = {4, 5, 6, 7, 8, 1}
print("A : ", A)
print("B : ", B)

print('Set Difference :', A.difference(B))
# or
print("Set Difference :", A - B)
print("\n")


# Example of Set Method
print('Set Method : ')


ss = {1, 9, 8}
s = {1, 2, 3, 4}

print('ss :', ss)
print('s  :', s)

# add five if it is not in set s
s.add(5)
print('add element :', s)


# for removing item to set
s.remove('remove  :', 2)
print(s)


# add ss set to set s
s.update(ss)
print('update    :', s)


# remove and return an element from set
print('pop       : ', s.pop())


# for cleaning all set
s.clear()
print('clear     : ', s)
print("\n")


# End of set :- 9:09 PM 6/12/2019

