""" This is the various variable types and their class
The first two lines just clear the output window
"""

import os
os.system("cls")

def nl(x):
    if not x:
        x=1
    for y in range(x):
        print('\n')

print("Control flow / loops")

for x in range(0,10):
    print(x, ' ', end="")

nl(1)
# break will exit the loop
for x in range(0,11):
    if x == 9:
        break
    print(x, ' ', end="")

nl(1)
# continue will skip over that iteration
for x in range(0,11):
    if x == 9:
        continue
    print(x, ' ', end="")

nl(1)

for x in range(3):
    print(x, ' ', end='')
else:
    print('\nFinal x = %d' % (x))

nl(1)

# Strings as an iterable
string = "Hello World"
for x in string:
    print(x, ' ', end='')

nl(1)

# list as an iterable
collection = ['hello', 333, 'world']
for x in collection:
    print(x, ' ', end='')

nl(1)

# list of lists ... 
list_of_lists = [ [1, 2, 3], ['abc', 'def', 'ghi'], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x, ' ', end='')
nl(1)

# create own range using yield
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
nl(1)
for x in my_range(1, 10, 0.5):
    print(x, ' ', end='')

nl(2)
#  _____________ WHILE __________________

count = 0
while count <= 5:
    print(count, ' ', end='')
    count += 1

nl(1)

# do .. while
condition = True
looped = 0
print("looped: ", end='')
while condition:
    print(looped, ' ', end='')
    looped += 1
    if looped > 5:
        condition = False
# end of loop