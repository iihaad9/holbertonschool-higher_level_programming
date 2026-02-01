#!/usr/bin/python3
"""Append text to a file and return the number of characters added."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
