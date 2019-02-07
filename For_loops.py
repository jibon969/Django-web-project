"""
    Python - Loops
"""


'''
What is for loop in Python?
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
Iterating over a sequence is called traversal.
'''


# Syntax of for Loop

"""
for i in range(10)
    print(i) 
    
Or

for val in sequence:
    Body of for	
"""


print("For Loop : ")

"""
Example 
"""

for i in range(10):
    print(i)

print("\n")


"""
Example 
"""

for i in range(1, 10):
    print(i, end=' ')

print("\n")


""" 
Write a program to print 1, 3, 5, 7
"""

for i in range(1, 10, 2):
    print(i, end="")

print("\n")


"""
Example 
"""

list = ["Python", "Django", "Php", "html", 'css']

for item in list:
    print(item)

print("\n")


"""
while লুপের মত ফর লুপেও break, continue ইত্যাদি কিওয়ার্ড ব্যবহার করে কাজের ধারাকে নিয়ন্ত্রণ করা যায়।
"""


for i in range(20):
    if i == 5:
        continue
    if i > 9:
        break
    print(i)

print("\n")


'''
Here "Python" acts like a list of characters
'''

for letter in 'Python':
    print(letter)

print('\n')


'''
Example: Python for Loop

'''

number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum = 0
# iterate over the list
for val in number:
    sum = sum + val
print(sum)
print('\n')


'''

Python break and continue
'''

for val in "string":
    if val == "i":
        continue
    print(val)
print('end loop')


'''
Python pass statement
'''

'''

What is pass statement in Python?
In Python programming, pass is a null statement. 
The difference between a comment and pass statement in Python is that,
while the interpreter ignores a comment entirely, pass is not ignored.

However, nothing happens when pass is executed. It results into no operation (NOP).
'''


'''
Syntax of pass
    pass
'''


'''
We generally use it as a placeholder.

Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. 
They cannot have an empty body. The interpreter would complain. 
So, we use the pass statement to construct a body that does nothing.
'''


'''
Example: pass Statement
'''

sequence = {'p', 'a', 's', 's'}

for var in sequence:
    pass
print("\n")


'''
We can do the same thing in an empty function or class as well.

def function(args):
    pass

class example:
    pass

'''


# Example

l = [1, 2, 3, 4, 5, 5]
for number in l:
    if number % 2 == 0:
        print('even number')
    else:
        print("Odd number")
print("\n")


# Example

l = [1, 2, 3, 4, 5]

list_sum = 0

for num in l:
    list_sum = list_sum + num

print(list_sum)

print("\n")


# Example

# l = 15 এর সাথে 2 যোগ করবে ।

l = [1, 2, 3, 4, 5]
list_sum = 2

for num in l:
    list_sum = list_sum + num

print(list_sum)



# Example


s = "This is a string"
for item in s:
    print(item)
print("\n")


# Example এইখানে This is a string ১৬ বার print করবে ।


s = "This is a string"
print(len(s))
for item in s:
    print(s)

print("\n")


# Example
tup = (1, 3, 4)
for tupple in tup:
    print(tupple)

print("\n")


# Example
l = [(1, 3, 5), (2, 4, 6), (7, 8, 9)]
for tupple in l:
    print(tupple)
print("\n")


# Example

d = {'k1': 1, "k2": 2, "k3": 3}
for item in d:
    print(item)

print('\n')


# Example

d = {'k1': 1, "k2": 2, "k3": 3}

for k, v in d.items():
    # print for all key
    print(k)
    # print all value
    print(v)

