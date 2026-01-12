#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        i = 0
        if n < 0:
            x = 1 / x
        res = x
        while i < abs(n) - 1:
            # print(f"i: {i}, res: {res}, x: {x}, n: {n}")
            res = res * x
            i += 1
        return res
# @lc code=end

