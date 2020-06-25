
class Solution:

    def is_palindrome(self, x: int) -> bool:
        if x >= 0 and x == int(str(x)[::-1]):
            return True


"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""