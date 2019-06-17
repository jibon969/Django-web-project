
# if else statement

"""
if কন্ডিশন সত্য হলে তার আওতাভুক্ত কোড ব্লকটি রান হয়। else বস্তুত if এর সাথেই সম্পর্কিত।
যদি if কন্ডিশনটি সত্য না হয় তাহলে else এর আওতাভুক্ত কোডব্লক রান বা এক্সিকিউট হয়।
"""

# Syntax of if...else

"""
if test expression:
    Body of if
else:
    Body of else

Or

if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false

"""
print("if else statement : \n")


# Example of if else

x = 4
if x == 5:
    print("it's 5")
else:
    print("it's not 5")
print("End program")
print('\n')


# Example of if else

i = 20

if i < 15:
    print(i, "is smaller than 15")
    print("i'm in if Block")

else:
    print(i, "is greater than 15")
    print("i'm in else Block")

print("i'm not in if and not in else Block")
print('\n')


# Example of if else
status = 1
msg = "logout" if status == 1 else "login"
print(msg)
print('\n')


# Example of Nested if else

a = 109
b = 208
c = 307

if a > b:
    if a > b:
        print("A is Large Number ", a)
    else:
        print("B is large number", b)
else:
    if b > c:
        print('Large Number is ', b)
    else:
        print("Large number is ", c)
print('\n')

# Example

username = input('Username: ')
password = input('Password: ')
if len(password) >= 6:
    print('Password is Strong')
else:
    print('Your password is not secured')
print('\n')


# Example of Password Match

username = ["jon", "joy", "wood"]
password = ['jon123', '123joy', 'wood260']

n = input('Username: ')
p = input('Password: ')
if n in username and p in password:
    print('Log in')
else:
    print('Username or password incorrect')
print("try again !")
print('\n')