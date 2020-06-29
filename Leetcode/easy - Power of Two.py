
class Solution:

    def is_power_of_two(self, n: int) -> bool:

        if n == 0:
            return False
        else:
            while n % 2 == 0:  # until number can be simply divisioned
                n /= 2         # devide it by "2"
            return n == 1      # return True


"""
Given an integer, write a function to determine if it is a power of two.
"""