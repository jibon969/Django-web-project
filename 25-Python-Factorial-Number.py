
# Start :- 11:29 PM 6/13/2019

# Python Factorial Number


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


x = 5
result = fact(x)
print('Factorial Number :', result)