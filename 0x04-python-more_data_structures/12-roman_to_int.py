#!/usr/bin/python3

def roman_to_int(roman_string):
    num_int = 0
    if roman_string is None or not isinstance(roman_string, str):
        return num_int
    roman_annot = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    i = 0

    while i < len(roman_string):
        present_num = roman_string[i]
        if (i + 1) < len(roman_string):
            next_num = roman_string[i + 1]
            if roman_annot[present_num] < roman_annot[next_num]:
                num_int -= roman_annot[present_num]
            else:
                num_int += roman_annot[present_num]
        else:
            num_int += roman_annot[present_num]
        i += 1
    return num_int
