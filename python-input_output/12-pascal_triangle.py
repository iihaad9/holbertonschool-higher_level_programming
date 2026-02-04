#!/usr/bin/python3
"""Generate Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last = triangle[-1]
            for j in range(1, i):
                row.append(last[j - 1] + last[j])
            row.append(1)
        triangle.append(row)

    return triangle
