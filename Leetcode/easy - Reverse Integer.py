
class Solution:
    def reverse(self, x: int) -> int:

        min_x = -2 ** 31
        max_x = 2 ** 31 - 1

        if x > 0:
            rev_x = int(str(x)[::-1])

        if x <= 0:
            rev_x = -1 * int(str(x * -1)[::-1])

        if rev_x in range(min_x, max_x):
            return rev_x

        else:
            return 0

"""
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

