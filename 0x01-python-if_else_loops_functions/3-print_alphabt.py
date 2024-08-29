#!/usr/bin/python3
for _ in range(97, 123, 1):
    if _ != ord("q") and _ != ord("e"):
        print("{}".format(chr(_)), end="")
