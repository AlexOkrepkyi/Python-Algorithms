class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i, num in enumerate(nums):
            if target - num in d:             # check, whether second number is in dictionary (has already be found previously)
                return d[target - num], i   # if so, return its index along with index of the current number
            d[num] = i                        # if not, add current number and its index to the dictionary

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""