#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if (my_list is None):
        return None
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)

