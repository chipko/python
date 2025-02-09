""" This is the various variable types and their class
The first two lines just clear the output window
"""

import os
os.system("cls")

print("Variables!\n----------")
text_string = "Hello World!"
print ("DATA:\t", text_string, "\t\t\t\tis of type\t\t", type(text_string))

integer = 12345789
print("DATA:\t", integer, "\t\t\t\tis of type\t\t", type(integer))

float = 12345.12345
print("DATA:\t", float, "\t\t\t\tis of type\t\t", type(float))

complex_num = 1j
print("DATA:\t", complex_num, "\t\t\t\t\tis of type\t\t", type(complex_num))

collection_set = {"a", "b", "c"}
print("DATA:\t", collection_set, "\t\t\tis of type\t\t", type(collection_set))

collection_list = ["a", "b", "c"]
print("DATA:\t", collection_list, "\t\t\tis of type\t\t", type(collection_list))

collection_tuple = (1,2,3,"hi")
print("DATA:\t", collection_tuple, "\t\t\tis of type\t\t", type(collection_tuple))

collection_dictionary = {1:"a",2:"b","c":"d"}
print("DATA:\t", collection_dictionary, "\t\tis of type\t\t", type(collection_dictionary))

boolean = True
print("DATA:\t", boolean, "\t\t\t\t\tis of type\t\t", type(boolean))

range_variable = range(33)
print("DATA:\t", range_variable, "\t\t\t\tis of type\t\t", type(range_variable))

frozen_set = frozenset({"a", "b", "c"})
print("DATA:\t", frozen_set, "\t\tis of type\t\t", type(frozen_set))

bytes_var = b"Hello"
print("DATA:\t", bytes_var, "\t\t\t\tis of type\t\t", type(bytes_var))

byte_array = bytearray(5)
print("DATA:\t", byte_array, "\tis of type\t\t", type(byte_array))

mem_view = memoryview(bytes(5))
print("DATA:\t", mem_view, "\tis of type\t\t", type(mem_view))

none_variable = None
print("DATA:\t", none_variable, "\t\t\t\t\tis of type\t\t", type(none_variable))

print("\n")
