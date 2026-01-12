#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        l = 0
        r = len(str(x)) - 1
        s = str(x)
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

