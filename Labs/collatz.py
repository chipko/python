import os
os.system("cls")
validnumber = False
print("Collat\'s hypnothesis:")

rownumber = 1

try:
    c0=int(input("Type a positive integer: "))
    print("Number:", c0)
    if c0 > 0:
        validnumber = True 

except ValueError:
    print("This is not a whole number.")

while (c0 != 1):
    if (c0 % 2 == 0):
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1

    print(c0, end="\n")