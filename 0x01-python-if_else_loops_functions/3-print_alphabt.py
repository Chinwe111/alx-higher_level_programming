#!/usr/bin/python3
#3-print_alphabt.py

for a in range(97, 123):
    if chr(a) is not 'q' and chr(a) is not 'e':
        print("{}".format(chr(a)), end="")
