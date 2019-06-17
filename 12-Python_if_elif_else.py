
# Start :- 9:40 PM 6/10/2019


# if elif else

"""
if test expression:
    Body of if
elif test expression:
    Body of elif
else:
    Body of else
"""


# মজার ব্যাপার হচ্ছে এরকম if else if এর চেইনকে একটু সংক্ষেপে elif দিয়েও লেখা যায়।
print("if elif else \n")


# Example of if elif else
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


# Example of if elif else

loc = "bank"
if loc == "Auto Shop":
    print('Welcome to Auto Shop')
elif loc == "bank":
    print("Welcome to the bank")
else:
    print("Where are you ?")
print('\n')


# Example

name = "jayed"
if name is "jewel":
    print("hello jewel")
elif name is 'jon':
    print("hi jon")
else:
    print("Hello", name)
print('\n')


# Example

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a > b:
    if a > c:
        print('a is greater than b,c')
    else:
        print('c is greater than a,b')
elif b > a:
    if b > c:
        print(print('b is greater than a,c'))
    else:
        print('c is greater than a,b')
else:
    if c > a:
        print(print('c is greater than a,b'))
    else:
        print('a is greater than b,c')
print("Bye")
print('\n')

# Now write a program to Academic Result

mark = int(input('Enter your mark :'))

if mark >= 80 and mark<=100:

    print('A + Grade ')

elif mark >= 75 and mark <=79:
    print('A Grade ')

elif mark >= 70 and mark <=74:
    print('A- Grade')

elif mark >=65 and mark <=69:
    print(' B+ Grade')

elif mark >= 60 and mark <=64:
    print('B Grade')

elif mark >= 55 and mark <=59:
    print('B- Grade')

elif mark >= 50 and mark <=54:
    print('C+ Grade ')

elif mark >= 45 and mark <=49:
    print('C Grade')

elif mark >= 40 and mark <=44:
    print('D Grade')

elif mark >= 00 and mark <=39:
    print('Fail try again')

else:
    print('\nNumber in not in range')
print("\n")


