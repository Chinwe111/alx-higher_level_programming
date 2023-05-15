#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list is None):
        return None
    maxVal = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxVal:
            maxVal = my_list[i]
    return (maxVal)
