#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordKey = sorted(a_dictionary.key())
    ordKey.sort()
    for i in ordKey:
        print("{}: {}".format(i, a_dictionary.get(i)))
