#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = len(nums) - 1
        while i > j:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[j]
                i += 1
            
            elif nums[i] == nums[j]:
                i += 1
            

        
# @lc code=end

