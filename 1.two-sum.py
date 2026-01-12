#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        k = {}
        for i in range(len(nums)):
            # print(k)
            t = target - nums[i]
            if t in k:
                return [k[t], i]
            k[nums[i]] = i
        return []

        
# @lc code=end

