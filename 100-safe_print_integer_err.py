#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except Exception:
        print("Exception: Unknown format code 'd' for object of type 'str'".format())
        return False
