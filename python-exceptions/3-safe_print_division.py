#!/usr/bin/python3
"""Safely divide two integers and print the result."""


def safe_print_division(a, b):
    """Divide two integers and print the result safely."""
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
