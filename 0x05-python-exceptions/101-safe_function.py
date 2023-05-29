#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
        return (output)
    except Exception as sys.exc_info()[1]:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
