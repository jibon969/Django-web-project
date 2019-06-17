
# Start :- 11:33 PM 6/13/2019

# Recursion Function

# Recursion Function যেই Function নিজে নিজেকে কল করে ।


# Example

import sys

sys.setrecursionlimit(200)
print(sys.getrecursionlimit)

i = 1


def greet():
    global i
    i = i + 1
    print('Hello :', i)


greet()

