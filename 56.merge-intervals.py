#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        s, e = intervals[0][0], intervals[0][1]
        for itv in intervals:
            if itv[0] <= e:
                e = max(e, itv[1])
            else:
                res.append([s, e])
                s = itv[0]
                e = itv[1]
        res.append([s, e])
        return res
# @lc code=end

