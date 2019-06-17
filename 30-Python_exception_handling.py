
# Start : 10:35 PM 6/16/2019

# File Exceptions

"""
    1. try
    2. except
    3. finally
"""


# Some Exceptions

""" 
try .....except

    1. FileNotFoundError
    2. ImportError
    3. IndentationError 
    4. StopIteration 
    5. ArithmeticError
    6. OverflowError 
    7. ZeroDivisionError
    8. ImportError 
    9. IndexError
    10. KeyError
    11. NameError
    12. IOError
    13. SyntaxError
    14. IndentationError
    15. RuntimeError
    16. ValueError
"""


"""
Exception হোল একটি ঘটনা, যা প্রোগ্রাম চলার সময় কোন সমস্যা হলে ঘটে ...... আমরা এই গুলো try ... except দ্বারা solve করতে পারি।

সাধারণ কোড গুলো try ব্লকে  মধ্যে থাকবে ... আর কোন Exception raise হলে except ব্লকে থাকবে ।

try ব্লকে এ যত খুশি তত except ব্লক লেখা যায় ...তবে প্রতিটি except ব্লকে Exception নাম লিখতেই হবে ।
"""
print('\n')


# Example of try ... except

# Example

a = 5
b = 0

try:
    print(a/b)

except Exception:
    print('Hey, you can not divided a number by zero')

print('Bye')
print('\n')


'''
a = 100
b = 0
c = a / b
print(c)

# এই কোডটি রান করলে আমারা নিচের এই Error টা পাবো ...

Traceback (most recent call last):

  File "F:/Python/Python-Code/Bangla-Blog/5-File & Exception/1-Try-Exception.py", line 43, in <module>
    print(a/b)
ZeroDivisionError: division by zero

'''

# উপরের এই problem টা আমারা solve করতে পারি try ... এন্ড except দ্বারা ।

try:
    a = 100
    b = int(input("Enter a divisor to divide 100: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")
print('\n')


# Example of try ... except

try:
    name = "Jibon"
    print(name/0)
except:
    print("An error occurred")

print('\n')


# Example try ... except ... else

# else ব্লক except ব্লক এর শেষে বসে । try ব্লকে কোন Exception raise না হইলে কেবল else ব্লক এর কোড executed হবে ।


try:
    x = 5
    y = 2
    print(x+y)

except ValueError as e:
    print(e)

else:
    print('There is no exception')

print('\n')


# Example of try ...except....finally
# finally ব্লক একেবারে শেষে বসে । আর কোন exception raise হোক আর নাই হোক finally ব্লকে কোড ঠিকই  executed হবে ।

try:
    print("Hello World !")
    print(1/0)

except ZeroDivisionError:
    print("Hi, ZeroDivisionError")

finally:
    print("This code will run ...")

print('\n')


'''
Raise exception
'''

# Python এ কিছু built-in Exception আছে । আর আমরা চাইলে এদেরকে raise করতে পারি ।


try:
    raise NameError("Hi, it is a custom Message")

except NameError as e:
    print(e)

