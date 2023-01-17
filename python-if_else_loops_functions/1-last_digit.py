#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if number < 0:
    x = -number % 10
if x < 6:
    print("Last digit of", number, "is", x, "and is less than 6 and not 0")
elif x > 5:
    print("Last digit of", number, "is", x, "and is greater than 5")
else:
    print("Last digit of", number, "is", x, "and is 0")
