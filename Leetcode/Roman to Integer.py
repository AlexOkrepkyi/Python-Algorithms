class Solution:

    def roman_to_integer(self, s: str) -> int:                                   # assume "MMMCDXVII" was given

        rev_s = s[::-1]                                                          # "IIVXDCMMM"
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = dic[rev_s[0]]

        if len(rev_s) > 1:
            for letter in range(1, len(rev_s)):                   # for "IIVXDCMMM" number range is [1, 9]
                if dic[rev_s[letter]] >= dic[rev_s[letter - 1]]:  # if next number > then the previous one:
                    num += dic[rev_s[letter]]                     # add it to the [num] variable
                else:                                             # if next number < then the previous one:
                    num -= dic[rev_s[letter]]                     # subtract it from the [num] variable
            return num
        else:
            return num  # if only 1 digit was given, return number


"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""