#!/usr/bin/python3

def no_c(my_string):
      """Remove all characters c and C from a string."""
    copy = ''
    for char in my_string:
        if (char != 'c' and char != 'C'):
            copy += char
    return ("".join(copy))
