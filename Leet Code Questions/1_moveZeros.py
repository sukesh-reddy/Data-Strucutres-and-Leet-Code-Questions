# Given an array nums, write a function to move all 0's to the end of it, while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        for num in nums:

            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index,n):
            nums[i] = 0
        print(nums)

        
