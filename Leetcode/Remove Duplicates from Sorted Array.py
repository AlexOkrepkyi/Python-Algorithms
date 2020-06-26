class Solution:

    def remove_duplicates(self, nums):  # assume we get [0,0,1,1,1,2,2,3,3,4]

        i = 0

        while i < len(nums) - 1:        # while index < 9 (i.e., 10 - 1)
            if nums[i] == nums[i + 1]:  # if current number == next number
                nums.remove(nums[i])    # remove current number
            else:
                i += 1                  # else proceed to the next index
        return len(nums)


