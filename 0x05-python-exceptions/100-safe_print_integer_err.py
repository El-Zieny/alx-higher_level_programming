#!/usr/bin/python3
def safe_print_integer_err(val):
    from sys import stderr
    try:
        print("{:d}".format(val))
        return True
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return False
