#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = 'f'
new_dict = simple_delete(my_dict, key)
print_sorted_dictionary(my_dict)
print("xx")
print_sorted_dictionary(new_dict)