#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
if number < 0:
    x = 10 - (number % 10)
    x = -x
else:
    x = number % 10
print(x, end="")
if x > 5:
    print(" and is greater than 5")
elif x == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
