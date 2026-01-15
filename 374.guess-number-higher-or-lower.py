#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            result = guess(mid)
            if result < 0:      # mid > pick, search lower half
                hi = mid - 1
            elif result > 0:    # mid < pick, search upper half
                lo = mid + 1
            else:
                return mid
        return -1
# @lc code=end

