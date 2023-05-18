#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_rom = 0

    for char in roman_string:
        if char not in rom_n:
            return 0
        list_rom = rom_n[char]

        if list_rom > last_rom:
            num += list_rom - 2 * last_rom
        else:
            num += list_rom

        last_rom = list_rom

    return num
