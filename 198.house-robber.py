#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        p, pp = 0, 0
        for i in range(len(nums)):
            temp = p
            p = max(p, pp + nums[i])
            pp = temp
        return p


# @lc code=end

