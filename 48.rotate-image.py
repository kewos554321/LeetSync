#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, 0
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                print(i, j)
        
        
# @lc code=end

