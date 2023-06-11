#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    if my_list == []:
        return None
    else:
        for num in my_list:
            if num > large:
                large = num
        return large
