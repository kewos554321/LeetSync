#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        car = 0
        while car or i >= 0 or j >= 0:
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0
            t = da + db + car
            car = t // 2
            rem = t % 2
            res.append(str(rem))
            i -= 1
            j -= 1

        
        return ''.join(reversed(res))




# @lc code=end

