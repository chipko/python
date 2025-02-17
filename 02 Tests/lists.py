# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
 
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
 
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")



my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("The list with unique elements only:")
print(unique_list)
