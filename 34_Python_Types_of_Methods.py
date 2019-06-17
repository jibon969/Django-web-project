
# Start : 3:34 PM 6/16/2019

# Types of Methods

"""
    1. Instance Method
    2. Class Method
    3. static method
"""

# Example


class Student:
    school = 'High School'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # average number
    def avg(self):
        return (self.m1 + self.m2 +self.m3)/3


s1 = Student(44, 45, 56)
s2 = Student(46, 45, 56)


print('average number :', s1.avg())
print('average number :', s2.avg())
print('\n')


# Method

"""
    Access or Method :- Fetch the value
    Mutator Method :- modify the value
    
    Or
    
    get : দ্বারা আমি ভালু কে Access করতে পারবো ।
    set : দ্বারা আমি ভালু কে change করা যায় । 
"""


# Example

class Teacher:
    school = 'ABC'

    def __init__(self, n1, n2, n3):

        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def s_avg(self):
        return self.n1 + self.n2 + self.n3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is teacher class')


t1 = Teacher(23, 34, 56)
t2 = Teacher(44, 65, 96)

print('Avg    :', t1.s_avg())
print('School :', Teacher.get_school())
print('Info   :', Teacher.info())