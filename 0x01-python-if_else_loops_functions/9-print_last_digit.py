#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    for i in range(number):
        if number > 9:
            number = number % 10
        else:
            break
    print(number, end="")
    return number
