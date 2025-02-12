import os
os.system("cls")

validnumber = False
print("Hello, let's check this pyramid thing!")

try:
    number=int(input("Type a number:"))
    print("Number:", number)
    validnumber = True 

except ValueError:
    print("This is not a whole number.")

if (validnumber):
    print("Now let's calculate!")