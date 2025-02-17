""" 
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
     """
var = 1

# Example 1:
print(var > 0)
print(not (var <= 0))
 
 
# Example 2:
print(var != 0)
print(not (var == 0))


i = 1
j = not not i

newlist = [1,2,3,4,5]
newlist.append(333)

print(newlist)

newlist.insert(2,444)
print(newlist)



variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

print("Var1:", variable_1)
print("Var2:", variable_2)