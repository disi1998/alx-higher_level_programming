#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(f"{len(argv) - 1} arguments.")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv), 1):
            print(f"{i}: {argv[i]}")
    else:
        print(f"{len(argv) - 1} argument:")
        print(f"1: {argv[len(argv) - 1]}")
