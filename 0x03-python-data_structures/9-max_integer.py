#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        large = my_list[0]
        for num in my_list:
            if num > large:
                large = num
        return large
