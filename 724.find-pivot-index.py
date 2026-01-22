#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        left = nums[0]
        right = nums[-1]
        while i < j:
            if left > right:
                right += nums[j]
                j-=1
            elif left < right:
                left += nums[i]
                i+=1
            else:
                i+=1
        return -1
# @lc code=end

