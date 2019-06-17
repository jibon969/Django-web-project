
# Start :- 8:17 PM 6/10/2019

#  Python Decision Making

"""
1. if
2. if else
3. if elif else
5. nested if
"""

# if statement

"""
পাইথনে if স্টেটমেন্ট ব্যবহার করে নির্দিষ্ট একটি কন্ডিশনের উপর ভিত্তি করে কিছু স্টেটমেন্ট বা কোড ব্লককে রান করানো যায়।
যদি একটি কন্ডিশন বা এক্সপ্রেশন সত্য হয় তাহলে এর আওতাভুক্ত স্টেটমেন্ট রান করবে ।
"""

# Python supports the usual logical conditions from mathematics

"""
    1. Equals: a == b
    2. Not Equals: a != b
    3. Less than: a < b
    4. Less than or equal to: a <= b
    5. Greater than: a > b
    6. Greater than or equal to: a >= b
"""

# Syntax of if Statement

'''
if test expression:
    statement(s)
'''

# Example of If statement

if True:
    print("I' am right")
print("Bye")
print('\n')


# Example of If statement

if 7 > 5:
    print("7 is bigger then 5")
print("End Program")
print('\n')


# Example

if 4 < 7:
    print("4 smaller than 7")   # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত
    print("Anything .... ")     # এই স্টেটমেন্টটিও if কন্ডিশনের এর আওতাভুক্ত
print("End Program")            # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত নয়
print("\n")


# Example :- If the number is positive, we print an appropriate message

num = 55
if num > 0:
    print(num, " is a positive number .")
print("Not a positive number")
print('\n')


# Example of Nested if statement

num = 17
if num > 5:
    print("Bigger than 5")
    if num <= 20:
        print("Between 6 and 20")
print("\n")
