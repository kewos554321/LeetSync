#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        sind, eind = 0, 0
        for i, itv in enumerate(intervals):
            if itv[0] < newInterval[0]:
                sind = i - 1
            elif itv[0] == newInterval[0]:
                sind = id

            if itv[1] < newInterval[1]:
                eind = i - 1
# @lc code=end

