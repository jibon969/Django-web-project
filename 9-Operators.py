
"""
    Operator in python
"""


'''

সাধারণ গণিতে যেমন যোগ বা বিয়োগের আগে গুন ও ভাগ করে নিতে হয় তেমনি প্রোগ্রামিং -এও এই অপারেটর গুলোর একটা অগ্রাধিকার মূলক নিয়ম আছে।

গণিতের সরল করার নিয়মের সাথেই মিলে যায় অর্থাৎ - প্রথমেই ব্র্যাকেটের কাজ, তারপর পাওয়ার/এক্সপোনেন্ট, অতঃপর গুন ও ভাগ এবং শেষে যোগ ও বিয়োগ।

Python language supports the following types of operators.

Arithmetic Operators

Comparison (Relational) Operators

Assignment Operators

Logical Operators

Bitwise Operators

Membership Operators

Identity Operators

In operator

not in Operator

'''
print("\n")




'''

Example 1 : Arithmetic operators

Operator        Description     Example

 +              addition        10 + 20 = 30
 -              Subtraction     20 - 10 = 10
 *              Multiplication  10 * 10 = 100
 /              Division        10 / 2  = 5
 %              Modulus         11 % 3  = 3.666666666
 **             power           3 ** 3  = 27
 //             Floor Division  11 // 3 = 3
 
'''

print("Arithmetic operators : \n")

print("10 + 20 = ", 10 + 10)

print("20 - 10 = ", 20 - 10)

print("10 * 5  = ", 10 * 5)

print("11 / 3  = ", 11 / 3)

print("11 % 3  = ", 11 % 3)

print("11 // 3 = ", 11 // 3)

print("2 ** 3  = ", 2 ** 3)

print("\n")




'''

Comparison or relational  operators in Python

Operator        Description	             Example

==              equal                   (a == b) is not true.
!=              not equal               (a != b) is true
>               greater than            (a > b) is not true.
<               less than               (a < b) is true.
>=              greater than or equal   (a >= b) is not true.
<=               less than or equal     (a <= b) is true.

'''


# Example
print("Comparison operators : \n")

a = 5
b = 9

print("5 == 9 = ", a == b)

print("5 != 9 = ", a != b)

print("5 > 9  = ", a > b)

print("5 < 9  = ", a > b)

print("5 >= 9 = ", a >= b)

print("5 <= 9 = ", a <= b)

print("\n")



'''
Assignment Operators

=   এটি হল a = 5
               
+=  এটি হল  c += a is equivalent to c = c + a
     
-=   এটি হল  c -= a is equivalent to c = c - a  

*=   এটি হল  c *= a is equivalent to c = c * a  

/=   এটি হল  c /= a is equivalent to c = c / a  
     
%=   এটি হল  c %= a is equivalent to c = c % a  

**=  এটি হল  c **= a is equivalent to c = c ** a  

//=  এটি হল  c //=  a is equivalent to c = c //=  a  

'''



print("Assignment Operators : \n")

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




print("Logical Operators : \n")

'''

Logical operators
Logical operators are the and, or, not operators.

'''


x = 6
y = 7

print('x and y : ', x == 6 and y == 9)
print('x or y  : ', x == 6  or y == 7)
print('not x   : ', not y)
print("\n")




'''

Bitwise operators

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

'''

print("Bitwise operators : ")

print('5 & 6 : ', 5 & 6)  # & Binary AND

print('5 | 6 : ', 5 | 6)  # | Binary OR

print('5 ^ 6 : ', 5 ^ 6)  # ^ Binary XOR

print('\n')


'''

Membership operators in Python

পাইথনে এই দুইটি অপারেটর আছে 

in এন্ড

not in

'''

print("Membership operators : \n")

a = "Bangladesh"
c = 'sh' in a
print("'sh' in a : ", c)
print('\n')


x = 'Hello world'

y = {1: 'F', 2: 'b'}

print("'H' in x : ", 'H' in x)

print("'hello' not in x : ",'hello' not in x)

print(1 in y)

print('a' in y)

print('\n')


'''
Identity Operators পাইথনে এই দুইটি অপারেটর  আছে তাহলো 

is এন্ড

is not

'''

print('Identity Operators : \n')

a = "Learn Python"
b = 12
c = a is b
print(c)
print('\n')

d =  a is not b
print(d)
print("\n")





print("Boolean : ")

'''
Boolean

বুলিয়ান হলো এক প্রকারের ডাটাটাইপ যার মান সবসময় কোন কিছু সত্য অথবা মিথ্যা বুঝায়।

সত্য ও মিথ্যাকে যথাক্রমে 1 ও 0 দ্বারা প্রকাশ করা হয়।

পাইথনে এই Boolean টাইপটির দুটি ভ্যালু আছে True এবং False

'''



# Boolean expression

'''
বুলিয়ান এক্সপ্রেশন হলো এমন কিছু এক্সপ্রেশন যেগুলো সত্য অথবা মিথ্যা মান রিটার্ন করে।
একাধিক বুলিয়ান এক্সপ্রেশন মিলেও একটি বুলিয়ান এক্সপ্রেশন বানানো যায়।
'''

# Boolean Operator

'''
বুলিয়ান টাইপের তিনটি বেসিক অপারেটর আছে। এরা হলো AND , OR , NOT
'''

# AND

'''
AND এর বেলায় যদি সবগুলো ভ্যারিয়েবল এর মান সত্য হয় তবে এক্সপ্রেশন টি সত্য হয়

অন্যথায় এক্সপ্রেশন টি মিথ্যা হয়।
'''


# Example of AND Operator
x = 5
y = 6

z = x == 5 and y == 6
print("And :", z)
print('\n')



# OR Operator

'''
OR এর বেলায় যদি কমপক্ষে একটি ভ্যারিয়েবল এর মান সত্য হয় তবে এক্সপ্রেশন টি সত্য হবে 

আর অন্যথায় এক্সপ্রেশন টি মিথ্যা ।

'''

"""
Example of OR
"""


x = 5
y = 6

z = x == 2 or y == 9
print("Or  :",z)
print("\n")




"""
NOT Operator
"""

a = not 13 > 7
print("not 3 > 2 : ", a)
print("\n")



'''
NOT একটি ইউনারি অপারেটর। এটি সাধারনত কোনো ভ্যারিয়েবল অথবা এক্সপ্রেশন এর বিপরীত ভ্যালু রিটার্ন করে।
'''

# Truth table

'''

A	B    A AND B	A OR B	 NOT A

0	0	   0	       0	     1
0	1	   0	       1	     1
1	0	   0	       1	     0
1	1	   1	       1	     0

'''


"""
এই বেসিক এপারেটর ছাড়াও আরো কিছু অপারেটর আছে যেগুলো হল যেমনঃ XOR,XAND,NAND,NOR
"""




# Some Example of Boolean Operator

"""
Example True
"""

a = True
print('True : ',a)
print(type(a))
print("\n")


"""
Example False
"""

b = False
print("False : ",b)
print(type(b))
print("\n")



"""
Example 
"""

a = 3
b = 9
print("a == b", a ==b)
print("\n")



"""
Example 1 != 1
"""

x = 1
y = 1

z = x != y
print("1 != 1 : ",z)
print("\n")


"""
Example of <
"""

a = 6
b = 9
c = a < b
print("6 < 9 : ",c)



"""
Example of >
"""

a = 6
b = 9
c = a > b
print("6 > 9 : ",c)

print("\n")



"""
Example of <=
"""

a = 70
b = 20
c = a <= b
print("10 <= 20 : ",c)
print('\n')


"""
Example of >=
"""

a = 70
b = 80
c = a >= b
print("90 >= 80 : ",c)
print("\n")



"""
Example
"""

x = bool(28)
print("bool(28)    : ", x)
print("\n")



"""
Example
"""

y = bool(-2.1996)
print("bool(-2.69) : ", y)
print("\n")



"""
Example
"""

z = bool(0)
print("bool(0)     : ", z)
print("\n")



"""
Example of Boolean String
"""

x = bool("Python")
print(x)
print("\n")




"""
Example
"""

b = bool(" ")
print(b)
print("\n")



"""
Example
"""
c = bool("")
print(c)
print("\n")



"""
Example 
"""

x = str(True)
print(x)
print("\n")



"""
Example 
"""
y = str(False)
print(y)
print("\n")



"""
 Example of int Boolean
"""

a = int(True)
print(a)
print('\n')



"""
Example
"""

b = int(False)
print(b)
print('\n')


"""
Example
"""

c = 5 + True
print("5 + True   : ", c)
print('\n')



"""
Example
"""

d = 10 * False
print("10 * False : ", d)
print("\n")



print("Bloean Logic ! ")


""" 
Boolean Logic 
if স্টেটমেন্টের জন্য জটিল কন্ডিশন তৈরির ক্ষেত্রে বুলিয়ান লজিক ব্যবহৃত হয়ে থাকে।
একটি if স্টেটমেন্ট যদি একাধিক কন্ডিশনের উপর নির্ভর করে সেখানে আমরা বুলিয়ান লজিক ব্যবহার করতে পারি।
পাইথনে and, or এবং not এই তিন ধরণের বুলিয়ান অপারেটর আছে।
অন্যান্য প্রোগ্রামিং ল্যাঙ্গুয়েজে এ ধরণের AND, OR বা NOT অপারেটরকে সাধারণত &&, ||, ! দিয়ে প্রকাশ করা হয় 

"""


# And

'''
এই  and অপারেটর দুটো আর্গুমেন্ট নিয়ে যাচাই করে এবং সত্য হয় যখন দুটো আর্গুমেন্টই সত্য হয়।
'''

a = 5
b = 6

x = a == 5 and b == 6
print("a == 5 and b == 6 : ", x)
print("\n")




# Example of or


'''
or এটি সত্য হয় যদি উক্ত দুটো আর্গুমেন্টের যেকোনো একটি সত্য হয়।
'''




"""
Example
"""

x = 3
y = 5

z = x == 3  or  y == 5
print("x == 3  or y == 5 : ",z)
print('\n')



"""
Example of not
"""


'''

অন্য দুটি অপারেটর এর মত not দুটো আর্গুমেন্ট নিয়ে কাজ করে না। 

বরং এর জন্য একটি আর্গুমেন্টই যথেষ্ট। এটি দিয়ে চেক করা হয় কোন লজিক না হয় কিনা। 

'''

x = not 1 == 3
print("not 1 == 3 : ",x)
print('\n')



"""
Example
"""

y = not 1 > 5
print("not 1 > 5  : ",y)
print('\n')



"""
Example
"""

a = 6
b = 7

c = 9
d = 10

x = a == b and c == d
print(x)
print('\n')
