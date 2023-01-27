#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return(0)
    dic = {"I": 1, "V": 5,"X": 10 ,"L": 50, "C": 100, "D": 500, "M": 1000}
    r = 0
    i = 0
    while (i < len(roman_string)):
        for j in dic:
            if (roman_string[i] == j):
                if i + 1 < len(roman_string):
                    if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                        r = r + 4
                    if roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                        r = r + 9
                    if roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                        r = r + 40
                    if roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                        r = r + 90
                    if roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                        r = r + 400
                    if roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                        r = r + 900
                r = r + dic[j]
        i = i + 1 
    return(r)
