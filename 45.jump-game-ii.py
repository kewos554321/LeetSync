#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        if not nums or len(nums) == 1:
            return 0

        end = len(nums) - 1
        farthest = 0
        jumps = 0

        while farthest >= end:
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
            i += 1
        

        
# @lc code=end

