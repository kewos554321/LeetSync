#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for c in s:
            if c.isalnum():  
                filtered.append(c.lower())  
        l = 0
        r = len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

