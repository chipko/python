import os
os.system("cls")

validnumber = False
print("Hello, let's check this pyramid thing!")

rownumber = 1

try:
    number=int(input("Type a number:"))
    print("Number:", number)
    validnumber = True 

except ValueError:
    print("This is not a whole number.")

if (validnumber):
    print("Now let's calculate!")
    while (number >= rownumber):
        number -= rownumber
        rownumber += 1
        # print("row:",number)
    else:
        print("Number of pyramid rows: ", rownumber)