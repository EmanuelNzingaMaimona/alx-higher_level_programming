#!/usr/bin/python3
def roman_to_int(roman_string):
    len_r = len(roman_string)
    sum_r = 0
    list_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or None:
        return 0
    else:
        for i in range(len_r):
            if i is (len_r - 1):
                sum_r += list_r[roman_string[i]]
            else:
                if list_r[roman_string[i]] >= list_r[roman_string[i + 1]]:
                    sum_r += list_r[roman_string[i]]
                else:
                    sum_r -= list_r[roman_string[i]]
    return sum_r
