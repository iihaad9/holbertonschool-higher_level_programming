#!/usr/bin/python3
"""Write text to a file and return the number of characters written."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
