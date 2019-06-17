
# Start :- 4:34 PM 6/16/2019


# Inner Class

"""
Inner class :- Inner class এর কাজ হোল একটি ক্লাস এর ভিতরে আরকটি  ক্লাস ।
Can we have a class inside of a class.
"""


# Example


class StudentInfo:

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll

# যখন আমারা object তৈরি করবো তখন আমাদেরকে value করতে হবে ।


x = StudentInfo('Jayed', 69)
y = StudentInfo('Jui', 70)


print('Name :', x.name, ', Roll :', x.roll)
print('Name :', y.name, ', Roll :', y.roll)

print('\n')


# Example of inner class


class Student:  # Outer class

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll
        # inner class access
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)

    # inner class
    class Laptop:   # inner class
        def __init__(self):
            self.band = "HP"
            self.cpu = "i5%"

        def inner_show(self):
            print(self.band, self.cpu)
        # এখন এই inner class কে কিভাবে access করবো ।


s1 = Student('Jayed', 4)
s2 = Student('Jui', 7)

print(s1.name, s1.roll)
print(s2.name, s2.roll)


# এখন এই inner class কে access করবো ।
lap1 = s1.lap.cpu
lap2 = s1.lap.band

print(lap1)
print(id(lap1))

print(lap2)
print(id(lap2))