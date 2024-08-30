#!/usr/bin/python3
for i in range(-122, -96, 1):
    if (i * -1) % 2 != 0:
        i = (i * -1) - 32
    else:
        i = i * -1
    print("{}".format(chr(i)), end="")
