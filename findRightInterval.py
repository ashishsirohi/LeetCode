# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.append(l[r][1] if r < len(l) else -1)
        return res



s = Solution()
nums = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
inp = []
for x, y in nums:
    inp.append(Interval(x,y))

print s.findRightInterval(inp)