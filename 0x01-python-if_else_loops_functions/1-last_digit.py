#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
text = "Last digit of"
i = 0
if number < 0:
    i = ((number * -1) % 10) * -1
else:
    i = number % 10
if i > 5:
    print(f"{text} {number} is {i} and is greater than 5")
elif i == 0:
    print(f"{text} {number} is {i} and is 0")
elif i < 6 and i != 0:
    print(f"{text} {number} is {i} and is less than 6 and not 0")
