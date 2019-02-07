
# Now Learn if statement

"""
পাইথনে if স্টেটমেন্ট ব্যবহার করে নির্দিষ্ট একটি কন্ডিশনের উপর ভিত্তি করে কিছু স্টেটমেন্ট বা কোড ব্লককে রান করানো যায়।

যদি একটি কন্ডিশন বা এক্সপ্রেশন সত্য হয় তাহলে এর আওতাভুক্ত স্টেটমেন্ট রান হয়।
"""


""" 
# Python if Statement Syntax

if test expression:
    statement(s)

"""


"""
Example
"""

if 7 > 5:
    print("7 is bigger then 5")

print("End Program")
print("\n")


"""
Example
"""

if 7 > 4:
    print("7 greater than 4")  # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত
    print("Anything .... ")   # এই স্টেটমেন্টটিও if কন্ডিশনের এর আওতাভুক্ত

print("End Program")  # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত নয়
print("\n")


"""
 if স্টেটমেন্টের আওতাভুক্ত বা আওতাভুক্ত নয়, এটি নির্ধারণ হয় indentation তথা স্টেটমেন্টের সামনে যথাযথ হোয়াইট স্পেস ব্যবহার করে।  

 পাইথনে indentation বাধ্যতামূলক অন্যথায় এরর তৈরি হবে।
"""


'''
Example :- If the number is positive, we print an appropriate message
'''

num = 4

if num > 0:
    print(num, 'is a positive number .')
print("This is always printed.")
print("\n")


# Example
num = -1
if num > 0:
    print(num, " is a  positive number .")
print("This is always printed.")
print("\n")


'''
Nested if statement
'''


"""
Example of Condition is True
"""

num = 17
if num > 5:
    print("Bigger than 5")
    if num <= 37:
        print("Between 6 and 37")

print("\n")


"""
Example of Condition is True
"""

num = 10
if num > 15:
    print("Bigger than 15")
    if num <= 37:
        print("Between 6 and 37")
    print("....")

print('End program .. ')


print("Python if...else Statement : ")


'''
Python if...else Statement

if কন্ডিশন সত্য হলে তার আওতাভুক্ত কোড ব্লকটি রান হয়। else বস্তুত if এর সাথেই সম্পর্কিত। 

যদি if কন্ডিশনটি সত্য না হয় তাহলে else এর আওতাভুক্ত কোডব্লক রান বা এক্সিকিউট হয়।

'''


# Syntax of if...else

'''
if test expression:
    Body of if
else:
    Body of else

'''


"""
Example 
"""

x = 5

if x == 7:
    print("It\'s 5")
else:
    print("it\'s not 7")

print("\n")


"""
Example 
"""

status = 'password'
mess = "Logout" if status == 'password' else "Login"
print(mess)
print("\n")


"""
Example 
"""

status = 7
mes = "Logout" if status == 5 else "Login"
print(mes)
print("\n")


'''
Syntax of if...elif...else

if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else

'''


"""
Example 
"""

num = 7
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")

print("\n")


'''
শুধুমাত্র if এর সাথে ব্যবহার বাদেও else কে ব্যবহার করা যায় for এবং while লুপের সাথেও।
'''

for i in range(1, 8):
    print(i)
else:
    print("Done")

"""
Example 
"""

name = "sakib"

if name is 'sakib':
    print("Hi Sakib")

elif name is 'jibon':
    print('Hi, Jibon')

else:
    print("Sakib is not here ! ")

print('\n')


"""
Example 
"""

number = 7

if number == 8:
    print("My Number is 4 ")

elif number == 7:
    print('My Number is 7')

else:
    print("What\'s you number ! ")

print('\n')


"""
Example of Nested if else
"""
a = 10
b = 2067
c = 2566565

if a > b:
    if a > b:
        print("A is Large Number ", a)
    else:
        print("B is large number", b)
else:
    if b > c:
        print('Large Numer is ', b)
    else:
        print("Large number is ", c)

print('\n')


'''
Write a program to take three number and which are are large
'''

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter third  Number : "))

if a > b:
    if a > b:
        print("A is Large Number : ", a)
    else:
        print("B is large number : ", b)
else:
    if b > c:
        print('B is Large Numer  :  ', b)
    else:
        print("C is Large number : ", c)

print('\n')


'''
    Python Nested if statements
'''


""" 
We can have a if...elif...else statement inside another if...elif...else statement. 
This is called nesting in computer programming.
"""

num = float(input("Enter a number : "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number ")
else:
    print("Negative Number ")

print("\n")



# Now write a program to Academic Result

mark = int(input('Enter your mark :'))

if mark >= 80 and mark <=100:

    print('A + Grade ')

elif mark >=75 and mark <=79:
    print('A Grade ')

elif mark >=70 and mark <=74:
    print('A- Grade')

elif mark >=65 and mark <=69:
    print(' B+ Grade')

elif mark >=60 and mark <=64:
    print('B Grade')

elif mark >=55 and mark <=59:
    print('B- Grade')

elif mark >=50 and mark <=54:
    print('C+ Grade ')

elif mark >=45 and mark <=49:
    print('C Grade')

elif mark >=40 and mark <=44:
    print('D Grade')

elif mark >=00 and mark <=39:
    print('Fail try again')

else:
    print('\nNumber in not in range')




