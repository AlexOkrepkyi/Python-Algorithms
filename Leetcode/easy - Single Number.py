
class Solution:

    def single_number(self, nums: List[int]) -> int:

        dic = {}

        for num in nums:
            if num not in dic:           # if number from the list is not in the dictionary
                dic[num] = 1             # add it
            else:
                dic[num] += 1            # else add 1 more

        for key, value in dic.items():
            if value == 1:               # return number [key], which occured only once [value] in the dictionary
                return key


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""