"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target: int):
        complement = dict()
        for idx, num in enumerate(nums):
            differend = target - num
            if differend in complement:
                return [idx, complement[differend]]
            complement[num] = idx

nums = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))    # [0, 1]