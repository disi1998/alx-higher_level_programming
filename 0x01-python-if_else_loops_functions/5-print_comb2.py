#!/usr/bin/python3
for _ in range(0, 100, 1):
    if _ < 99:
        print("{:02}, ".format(_), end="")
    else:
        print("{}".format(_))
