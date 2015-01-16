# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x.start)
        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                if res[len(res)-1].start<=intervals[i].start<=res[len(res)-1].end:
                    res[len(res)-1].end = max(intervals[i].end,res[len(res)-1].end)
                else:
                    res.append(intervals[i])
        return res
