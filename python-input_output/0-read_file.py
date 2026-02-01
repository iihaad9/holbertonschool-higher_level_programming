#!/usr/bin/python3
"""Read a UTF-8 text file and print its contents to stdout."""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
