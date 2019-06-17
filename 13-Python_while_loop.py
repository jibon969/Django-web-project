
# Start :- 9:37 AM 6/11/2019

# while loop (Indefinite Iteration)


# while loop কেন ব্যবহার করবো

"""
We generally use this loop when we don't know beforehand (নির্দিষ্ট সময়ের পূর্বেই ),the number of times to iterate.
"""


# while loop কে কন্ট্রোল করার জন্য আমারা break ও continue ব্যবহার করা হয় ।


# Syntax of while Loop in Python

"""
while test_expression:
    Body of while
    
Or

while <expr>:
    <statement(s)>
    
    
# while loop with else

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
    
"""

# Example of while loop


i = 1    # initialization
while i < 10:   # condition
    print(i)
    i = i + 1   # increment/de-increment

print('\n')


# Example while loop with else

x = 0
while x < 10:
    print("x is currently : ", x)
    x = x + 1
else:
    print('All Done !')

print('\n')


# Example while loop with else

counter = 1

while counter < 5:
    print("Inside Loop", counter)
    counter = counter + 1
else:
    print('Inside else and Stop program !')
print("\n")


# Print 1 to 10

i = 1
while i <= 10:
    print('Number ', i)
    i += 1
print('\n')


# print to 10 to 1

i = 10
while i >= 1:
    print("Number ", i)
    i = i - 1

print('\n')


# Example of even number

i = 2
while i <= 10:
    print('Even Number ', i)
    i = i + 2

print('\n')


# Example of odd number

i = 1
while i <= 10:
    print('odd Number ', i)
    i = i + 2

print('\n')


# while ব্যবহার করে আমারা even number ও odd number বের করবো ।
print('Even number || odd number')

n = 2
while n <= 10:
    if n % 2 == 0:
        print('Even Number ', n)
    else:
        print("Odd Number ", n)
    n = n + 2

print('\n')


# print 1 to 100 মধ্যে ৫ ঘর পর পর ভালু গুলো প্রিন্ট করবে

n = 0

while n < 100:
    print(n, end=' ')
    n = n + 5
print('\n')


# print 1 + 2 + 3 + 4 + 5 = total sum

n = 1
temp = 0
while n <= 10:
    temp = temp + n
    n = n + 1
print("sum : ", temp, end=" ")

print("\n")


# user input from any number and there sum

user_input = int(input("Enter any number : "))

n = 1
temp = 0
while n <= user_input:
    temp = temp + n
    n = n + 1
print("sum of : ", temp, end=" ")

print("\n")


# Example how to print multiplication table নামতা প্রিন্ট করবো ।

userInput = int(input("Multiplication Enter your number : "))
n = 1
while n <= 10:
    print(userInput, '*', n, '=', userInput * n)
    n += 1

print('\n')


# Example of infinite loop

while 1 == 1:
    print("infinite loop")
    break
print('\n')


# Example of break
print('break statement \n')

i = 2
while i <= 20:
    print(i)
    if i == 8:
        break
    i = i + 1
print('\n')


# Example of continue
print("The continue Statement : \n")


i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)
print('\n')


# Break, continue, pass
print('Break, continue, pass \n')


x = 0
while x < 10:
    print("x is currently :", x)
    print("x is still less then 10, adding 1 to x")
    x += 1
    if x == 3:
        print('x is equal to 3')
        break
    else:
        print("continue ....")
        continue

print('\n')


# Example of char
i = 0
while i <= 150:
    print(i, '-', chr(i))
    i = i + 1
print('\n')


# End 11:46 AM 6/11/2019
