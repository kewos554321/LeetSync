#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        j = 0
        while i < l and j < l:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1





# @lc code=end

