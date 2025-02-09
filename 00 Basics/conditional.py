""" This is the various variable types and their class
The first two lines just clear the output window
"""

import os
os.system("cls")

# if .. elif .. else
x = 4
y = 2
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is not greater than y")

a = 1
if a % 2 == 0:
    print('even')
else:
    print('odd')
# odd


# Ternary expressions
# X if condition else Y
a = 1
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# odd
a = 2
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# even

# Ternary expressions with more conditional expressions
# 1. X if condition1 else (Y if condition2 else Z)
# 2. (X if condition1 else Y) if condition2 else Z
a = -2
result = 'negative' if a < 0 else 'positive' if a > 0 else 'zero'
print(result)
# negative
result = 'negative' if a < 0 else ('positive' if a > 0 else 'zero')
print(result)
# negative
result = ('negative' if a < 0 else 'positive') if a > 0 else 'zero'
print(result)
# zero


# Lambda expressions:
get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'
print(get_odd_even(1))
# odd
print(get_odd_even(2))
# even



