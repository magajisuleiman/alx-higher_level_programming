#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except(ZeroDivisionError):
            print("division by {}".format(my_list_2[i]))
            div = 0
        except(TypeError):
            print("wrong type".format())
            div = 0
        except(IndexError):
            print("out of range".format())
            div = 0
        finally:
            div_list.append(div)
    return (div_list)
