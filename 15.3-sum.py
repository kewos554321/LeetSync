#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for k in range(len(nums) - 2):
            i, j = k + 1, len(nums) - 1
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                # print(f't={total}, k={nums[k]}, i={nums[i]}, j={nums[j]}')
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(res)

# @lc code=end

