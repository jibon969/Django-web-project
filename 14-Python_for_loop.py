
# Start :- 11:53 AM 6/11/2019

# What is for loop in Python ?

"""
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
"""


# Syntax of for Loop
"""
for val in sequence:
    Body of for
"""


# Example

print('Print 0 to 10 :')
for i in range(10):  # Python default 0 to start for loop
    print(i)
print('\n')


# How to  print 1, 3, 5, 7  using for loop

print('How to print 1 3 5 .... 50 :\n')
for i in range(1, 49, 2):  # Here 1 start point, 10 end point, 2 step কতঘর পর প্রিন্ট হবে ।
    print(i, end=' ')
print('\n')


# Example of break

print('for loop using break : ')
for number in range(1, 20):
    if number == 5:
        break
    print(number)

print('\n')


# Example of continue


print('for loop using continue : \n')
for number in range(1, 10):
    if number == 5:
        continue
    print(number, end=' ')

print('\n')


# Example of  continue, pass, break


print('continue, pass, break using for loop : ')

for i in range(10):
    if i == 5:
        continue
    if i == 7:
        pass
    if i == 9:
        break
    print(i, end=' ')
print('\n')


# How to print letter

print('How to print letter : ')
for letter in 'word':
    print(letter)
print('\n')


# Example of list using for loop
print('List using for loop : ')

myList = ["Python", "Django", "Php", "html", 'css']
for item in myList:
    print(item)
print("\n")


# Example of string using for loop
print('string using for loop : ')

s = "Hi, there how are you"
for st in s:
    print(st, end=' ')
print('\n')


# Example of tuple using for loop
print('tuple using for loop : ')

tup = (1, 3, 5, 7, 9)
for t in tup:
    print(t)
print('\n')


# Example of dictionary using for loop
print('Dictionary using for loop : ')


d = {'k1': 1, 'k2': 3, 'Name': 'Hello', 'Age': 23 }
for k, v in d.items():
    print(k, end=' ')    # print for all key
    print(v, end=' ')    # print all value

print('\n')


# Example of list item and sum
print('Print list item sum : \n')


new_list = [1, 2, 3, 4, 5]
list_sum = 0

for num in new_list:
    list_sum = list_sum + num
print('sum =', list_sum)
print("\n")


# Print all the perfect sequence number between 1 to 50 who divided 3 or 5 == 0
# 1 থেকে 50 প্রজন্ত যারা ৩ ও ৫ দ্বারা ভাগকরলে ভাগফল ০ হবে ।


print('Perfect sequence number : \n')
for number in range(1, 50):
    if number % 3 == 0 or number % 5 == 0:
        continue
    print(number, end=' ')

print('\n')


# Example
print("How to print : \n")

# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(4):
        print('#', end=' ')
    print('#')
print('\n')


# Example of star

"""
*
* *
* * *
* * * * 
* * * * * 
"""

for i in range(5):
    for j in range(i + 0):
        print('*', end=' ')
    print('*')

print('\n')


# Example

"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(7):
    for j in range(6 - i):
        print('*', end=' ')
    print('*')
print('\n')


# Example of char symbols
print('char symbols :\n')

for i in range(100):
    print(i, '-', chr(i))
print('\n')

# End program :-  1:38 PM 6/11/2019

