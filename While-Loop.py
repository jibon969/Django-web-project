
"""
    While loop
"""

print('\n')


"""
While loop in python
"""

'''
What is while loop in Python?

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

while loop কেন ব্যবহার করবো 
We generally use this loop when we don't know beforehand, the number of times to iterate.

'''


'''
Syntax of while Loop in Python

while test_expression:
    Body of while
'''


'''
Now write a program to print 1 to 10
'''

print('Wile loop : ')

i = 1

while i <= 10:
    print(i, end=" ")
    i = i + 1

print("\n")


'''
while loop with else
'''

counter = 0

while counter < 3:
    print("Inside Loop")
    counter = counter + 1
else:
    print('inside else')


'''
print even number 2 to 10
'''

a = 2
while a <= 10:
    print("even number : ", a)
    a = a + 2

print("\n")


'''
print odd number 1 to 9
'''

x = 1

while x <= 9:
    print("Odd number :", x)
    x = x + 2

print("\n")


'''
print 1 to 20 মধ্যে ৫ ঘর পর পর ভালু গুলো প্রিন্ট করবে
'''
c = 1

while c <= 20:
    print(c)
    c = c + 5

print("\n")


'''
write a program to print 9, 8, 7, 6, 5
'''


z = 9

while z >= 5:
    print(z)
    z = z - 1

print("\n")


'''
1 + 3 + 5 there sum
'''

n = 1
temp = 0
while n <= 5:
    temp = temp + n
    n = n + 2
print("sum : ", temp,end=" ")

print("\n")


'''
নামতা প্রিন্ট করবো ......।
'''

a = 3
n = 1
while n <= 10:
    print(a, "*", n, '=', a*n)
    n = n + 1

print("\n")


'''
User input print Nomenclature বা নামতা
'''

user_input = int(input("Enter a number : "))

n = 1

while n <= 10:
    print(user_input, "*", n, " = ", user_input*n)
    n = n + 1

print("\n")


'''
Break
'''

i = 2
while i <= 20:
    print(i)
    if i == 8:
        break
    i = i + 1
print("Best of luck .......")