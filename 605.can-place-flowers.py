#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        j = 1
        maxV = 0
        while j < len(flowerbed):
            if flowerbed[i] + flowerbed[j] == 0:
                maxV += 1
            i+=2
            j+=2
        return n <= maxV

# @lc code=end

