#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/zenwa/ALX/main/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 9, in add_integer
        raise TypeError("b must be an integer")
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/zenwa/ALX/main/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 7, in add_integer
        raise TypeError("a must be an integer")
    TypeError: a must be an integer
    >>> add_integer(50, 50)
    100
    >>> add_integer(50, 52)
    102
    >>> add_integer(-30, -20)
    -50
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    c = a +b

    return c
