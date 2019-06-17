

# importing built-in module math
import math
print('importing built-in module math :- \n')


print('sqrt      :', math.sqrt(25))


# using pi function contained in math module
print('Math      :', math.pi)


# 2 radians = 114.59 degreees
print('degreees  :', math.degrees(2))


# # 60 degrees = 1.04 radians
print('radians   :', math.radians(60))

# Sine of 2 radians
print('sin       :', math.sin(2))


# Cosine of 0.5 radians
print('cos       :', math.cos(0.5))


# Tangent of 0.23 radians
print('tan       :', math.tan(0.23))


# 1 * 2 * 3 * 4 = 24
print('factorial :', math.factorial(4))
print('\n')


# importing built in module random
print('importing built in module random :- \n')


import random

# printing random integer between 0 and 5
print('randint  :', random.randint(0, 5))

# print random floating point number between 0 and 1
print('random   :', random.random())

# random number between 0 and 100
print('random   :', random.random() * 100 )

List = [1, 4, True, 800, "python", 27, "hello"]

# using choice function in random module for choosing
# a random element from a set such as a list
print('random choice :', random.choice(List))
print('\n')
