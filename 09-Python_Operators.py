
# Start :-  3:06 PM 6/10/2019

# Python Operator


"""
1. সাধারণ গণিতে যেমন যোগ বা বিয়োগের আগে গুন ও ভাগ করে নিতে হয়
তেমনি প্রোগ্রামিং - এই অপারেটর গুলোর একটা অগ্রাধিকার মূলক নিয়ম আছে।

2. গণিতের সরল করার নিয়মের সাথেই মিলে যায় অর্থাৎ -
প্রথমেই ব্র্যাকেটের কাজ, তারপর পাওয়ার/এক্সপোনেন্ট, অতঃপর গুন ও ভাগ এবং শেষে যোগ ও বিয়োগ।
"""


# Python language supports the following types of operators.

""" 
    1.  Arithmetic Operators
    2.  Comparison (Relational) Operators
    3.  Assignment Operators
    4.  Logical Operators
    5.  Bitwise Operators
    6.  Membership Operators
    7.  Identity Operators
    8.  In operator
    9.  not in Operator
    10. In Plus Operator in python
"""
print("\n")


# Example of Arithmetic operators

'''
Operator        Description     Example

 +              addition        10 + 20 = 30
 -              Subtraction     20 - 10 = 10
 *              Multiplication  10 * 10 = 100
 /              Division        10 / 2  = 5
 %              Modulus         11 % 3  = 3.666666666
 **             power           3 ** 3  = 27
 //             Floor Division  11 // 3 = 3

'''

print("Arithmetic operators : ")

print("10 + 20 = ", 10 + 10)
print("20 - 10 = ", 20 - 10)
print("10 * 5  = ", 10 * 5)
print("11 / 3  = ", 11 / 3)
print("11 % 3  = ", 11 % 3)
print("11 // 3 = ", 11 // 3)
print("2 ** 3  = ", 2 ** 3)
print("\n")


# Comparison or relational  operators in Python

'''
Operator        Description	             Example

==              equal                   (a == b) is not true.
!=              not equal               (a != b) is true
>               greater than            (a > b) is not true.
<               less than               (a < b) is true.
>=              greater than or equal   (a >= b) is not true.
<=               less than or equal     (a <= b) is true.

< এর ভালু বড় ।

এর ভালু বড় > । 

'''

print("Comparison operators : ")

a = 5
b = 9

print("5 == 9 = ", a == b)
print("5 != 9 = ", a != b)
print("5 > 9  = ", a > b)
print("5 < 9  = ", a > b)
print("5 >= 9 = ", a >= b)
print("5 <= 9 = ", a <= b)
print("\n")


# Assignment Operators

'''
=   এটি হল a = 5

+=  এটি হল  c += a is equivalent to c = c + a

-=   এটি হল  c -= a is equivalent to c = c - a  

*=   এটি হল  c *= a is equivalent to c = c * a  

/=   এটি হল  c /= a is equivalent to c = c / a  

%=   এটি হল  c %= a is equivalent to c = c % a  

**=  এটি হল  c **= a is equivalent to c = c ** a  

//=  এটি হল  c //=  a is equivalent to c = c //=  a  

'''

print("Assignment Operators : ")

a = 10
b = 5

c = a + b
print("10 + 5:", c)


#  += Add AND
c += a
print('15 += 10  : ', c)


# -= Subtract AND
c -= a
print('10 -= 5   : ', c)


# *= Multiply AND
c *= a
print('15 *= 10  : ', c)


#  /= Divide AND
c /= a
print('15 /= 10  : ', c)


# %= Modulus AND
c %= a
print('15 %= 10  : ', c)


# **= Exponent AND
c **= a
print('15 **= 10 : ', c)


#  //= Floor Division
c //= a
print('15 //= 10 : ', c)
print("\n")


# Logical operators

""" 
    Logical operators are the and, or, not operators.
    Logical operators boolean value return করে । 
"""

# Truth table

'''
A	B    A AND B	A OR B	 NOT A

0	0	   0	       0	     1
0	1	   0	       1	     1
1	0	   0	       1	     0
1	1	   1	       1	     0

'''

# Example of and
# and এর condition হোল যদি দুইটি condition সত্য হলে অন্যথায় false .

print("Logical operators : ")
a = 5
b = 6
c = a == 5 and b == 6
print('and = ', c)


# Example of or
# or এর condition হোল যে কোন একটি condition সত্য হলে অন্যথায় false .

a = 5
b = 6
c = a == 5 or b == 6
print('or = ', c)


# NOT একটি ইউনারি অপারেটর। এটি সাধারনত কোনো ভ্যারিয়েবল অথবা এক্সপ্রেশন এর বিপরীত ভ্যালু রিটার্ন করে।

# Example of not
x = 2!= 3
print('not = ', x)
print('\n')


# Bitwise Operators

"""
Bitwise operator works on bits and performs bit by bit operation.

Assume if a = 60; and b = 13; Now in binary format they will be as follows −

a = 0011 1100

b = 0000 1101

Operator	Meaning	                Example

&	        Bitwise AND	            x & y       = 0 (0000 0000)
|	        Bitwise OR	             x | y      = 14 (0000 1110)
 ~	        Bitwise NOT	            ~x          = -11 (1111 0101)
^	        Bitwise XOR	            x ^ y       = 14 (0000 1110)
>>	        Bitwise right shift	    x>> 2       = 2 (0000 0010)
<<	        Bitwise left shift	    x<< 2       = 40 (0010 1000)
"""

print("Bitwise operators : ")

print('5 & 6 : ', 5 & 6)  # & Binary AND
print('5 | 6 : ', 5 | 6)  # | Binary OR
print('5 ^ 6 : ', 5 ^ 6)  # ^ Binary XOR
print('\n')


# Membership operators in Python
# পাইথনে এই দুইটি অপারেটর আছে  in এন্ড not in

print("Membership operators : ")

a = "Bangladesh"
c = 'sh' in a
print("'sh' in a : ", c)
print('\n')


# Identity Operators পাইথনে এই দুইটি অপারেটর  আছে তাহলো is এন্ড is not
print('Identity Operators : ')


# Example of is operator

a = "Learn Python"
b = 12

c = a is b
print('is operator =', c)


# Example of is not
d = a is not b
print('is not operator = ', d)
print("\n")


# Chained Comparison Operators

# এই Operators এর কাজ হোল একশাথে multiple Comparison চেক করতে পারি ।
print("Chained Comparison Operators : ")


a = 1 < 2 and 2 > 4
print(a)

# Example

x = 1 < 3 > 2
print(x)
