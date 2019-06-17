
# Start :- 11:06 AM 6/14/2019

from create_module import *     # Everything import from create_module

a = int(input('Enter First  Number : '))
b = int(input('Enter Second Number : '))

c = add(a, b)
d = sub(a, b)
e = mul(a, b)
f = div(a, b)

print('add :', c)
print('Sub :', d)
print('mul :', e)
print('div :', f)
print('\n')


# Or

# from create_module import add, sub, div, mul

import create_module

print('Import Module 2 :\n')
a = int(input('Enter First  Number : '))
b = int(input('Enter Second Number : '))


c = create_module.add(a, b)
d = create_module.sub(a, b)
e = create_module.mul(a, b)
f = create_module.div(a, b)

print('add :', c)
print('Sub :', d)
print('mul :', e)
print('div :', f)
print('\n')

