
# Start :- 9:57 PM 6/16/2019

# Polymorphism Operator Overloading

a = 5
b = 6

print(a+b)
print(int.__add__(a, b))
print('\n')


# Example

x = '5'
y = '6'
print(a + b)
print(str(a+b))
print('\n')


# Example

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)
        return m3


s1 = Student(66, 97)
s2 = Student(84, 55)
s3 = s1 + s2
print(s3.m1)

