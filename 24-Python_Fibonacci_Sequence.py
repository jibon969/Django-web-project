
# 11:18 PM 6/13/2019

# Fibonacci Sequence

"""
Fibonacci Sequence. The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it.
"""


# Example

def fib(n):

    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


fib(8)


# End :- 11:27 PM 6/13/2019




