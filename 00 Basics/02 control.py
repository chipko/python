""" This is the various variable types and their class
The first two lines just clear the output window
"""

import os
os.system("cls")

print("Control flow / loops")

for x in range(0,10):
    print(x, ' ', end="")

print('\n')
# break will exit the loop
for x in range(0,11):
    if x == 9:
        break
    print(x, ' ', end="")

print("\n")
# continue will skip over that iteration
for x in range(0,11):
    if x == 9:
        continue
    print(x, ' ', end="")

