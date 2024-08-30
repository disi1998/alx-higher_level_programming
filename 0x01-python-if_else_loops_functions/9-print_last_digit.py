#!/usr/bin/python3
def print_last_digit(number):
    i = 0
    if number < 0:
        i = (number * -1) % 10
        print("{}".format(i), end="")
    else:
        i = number % 10
        print("{}".format(i), end="")
    return i
