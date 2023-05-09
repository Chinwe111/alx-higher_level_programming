#!/usr/bin/python3
#3-print_alphabt.py

"""Print the alphabet except q and e, not followed by a new line"""
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
