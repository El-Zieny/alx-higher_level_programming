#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        t = i % 3
        f = i % 5
        if t == 0 and f == 0:
            print("FizzBuzz", end=" ")
        elif t == 0:
            print("Fizz", end=" ")
        elif f == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
