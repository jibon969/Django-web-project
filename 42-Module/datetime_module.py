
# 12:17 PM 6/14/2019

# Python Datetime Module


print("Python Datetime Module : \n")

"""
    The Python datetime module offers functions and classes for working with 
    date and time parsing, formatting, and arithmetic.
"""

# Example

import datetime

x = datetime.MAXYEAR
print("Max year : ", x)
print("\n")


# Example

b = datetime.MINYEAR
print("MINYEAR : ", b)
print("\n")

# Example

c = type(datetime.MAXYEAR), type(datetime.MINYEAR)
print("type : ", c)


# Example

a = datetime.datetime.now()
print("Datetime : ", a)
print("\n")


# Python date Objects
print("Python date Objects : \n")


# date(year, month, day)

d = datetime.date(2019, 3, 19)
print("year, month, day : ", d)
print("\n")


# Example

"""
today() will return the current local date.
"""

x = datetime.date.today()
print("today : ", x)
print("\n")


# from timestamp(timestamp)
print("timestamp : ")

"""
fromtimestamp will return the date for the Python timestamp provided.
"""
import time
d = time.time()
print("time : ", d)
print("\n")

# Example

d = datetime.date.fromtimestamp(time.time())
print("fromtimestamp : ", d)
print("\n")


# Example

# date.min It returns the earliest representable date.

import datetime

d = datetime.date.min
print("date.min : ",  d)
print("\n")


# date.max
# Like min, max returns the latest representable date.

d = datetime.date.max
print("date.max : ",  d)
print("\n")


# This returns the year from a date object.

d = datetime.date(2019, 3, 19)
print("year : ", d)


# day

x = d.day
print("day : ", x)


# month

x = d.month
print("day : ", x)


# Example timetuple() returns a tuple of attributes for the current local time.

x = d.timetuple()
print('timetuple : ', x)
print("\n")


# Python time Objects
print("Python time Objects : \n")

t = datetime.time(11, 59, 59, 99999)
print("Python time Objects : ", t)


# Example max
# This returns the earliest representable time.

d = t.max
print("max : ", d)


# Example min
# This returns the latest representable time.

d = t.min
print("min : ", d)


# Example resolution
# resolution returns the smallest possible difference between non-equal time objects.

d = t.resolution
print("resolution : ", d)


# hour
# This tells us the hour from the object.


d = t.hour
print("hour : ", d)


# Example minute
# This returns the minute.

d = t.minute
print("minute : ", d)


# Example microsecond
# This returns the microsecond.

d = t.microsecond
print("minute : ", d)


# Example second
# This returns the second


d = t.second
print("second : ", d)


# Example tzinfo
# This returns whatever we pass as tzinfo to the object while creating it. If we didn’t, it returns None.


d = t.tzinfo
print("tzinfo : ", d)


# Resources from

# link : https://data-flair.training/blogs/python-datetime-module/



