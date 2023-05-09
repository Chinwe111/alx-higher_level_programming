#!/usr/bin/python3
# 10-add.py


def add(a, b):
    """Return the addition of a and b."""
    add = __import__(a + b).add
    print(add(a, b))
