#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] == idx:
                del my_list[idx]
            else:
                new_list = my_list
        return new_list
