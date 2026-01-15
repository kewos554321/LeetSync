#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for i in t:
            if len(s) == 0:
                break
            if s[0] == i:
                s.pop(0)
        return len(s) == 0
# @lc code=end

