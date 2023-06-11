#!/usr/bin/python3ccle a  
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in my_list:
            print("{:d}".format(my_list[len(my_list) - i]))
