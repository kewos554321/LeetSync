#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        if length == 0 or length == 1: 
            return nums
        print(f'length {length}')
        i = 0
        while i < length - 2:
            print(f'nums {nums}')
            if nums[i] != 0:
                i += 1
            else:
                j = i + 1
                print(f'i {i} j {j}')
                while j < length - 1:
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
                i += 1
 

# @lc code=end

