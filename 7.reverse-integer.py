#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow
            if (val > 214748364 or (val == 214748364 and digit > 7)):
                return 0
            if (val < -214748364 or (val == -214748364 and digit < -8)):
                return 0
            
            val = val * 10 + digit
        return val
# @lc code=end

