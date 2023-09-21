# Two Sum

"""
Given an array of integer "nums" and an integer "target", return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15] target = 9
Output: [0,1]
Explanation: Bracuse nums[0] + nums[1] == 9, we return [0,1]

"""
from typing import List


class Solution:
    # time comp -- > O(n^2), Space Comp --> O(1)
    def toSum(self, nums: List[int], target):
        for i in range(0, len(nums) - 1): # 0 .. 3 --> i = 0, j = 1, i = 1, J=2
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return None

    # time comp -- > O(n), Space Comp --> O(n)
    def toSum2(self, nums: List[int], target):
        myHashMap = {}
        for ix, num in enumerate(nums):
            difference = target - num
            if difference in myHashMap:
                return [myHashMap[difference], ix]
            myHashMap[num] = ix


sol = Solution()
print(sol.toSum([2, 7, 11, 15], 9))
print(sol.toSum([3, 2, 4], 6))
print(sol.toSum([3, 2, 4, 5], 9))

print(sol.toSum2([10,2, 4, 5, 8], 7))