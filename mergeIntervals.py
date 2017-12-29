# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)

        index = 1
        while index < len(intervals):
            if intervals[index - 1].end >= intervals[index].start:
                tmp = Interval()
                tmp.start = min(intervals[index - 1].start, intervals[index].start)
                tmp.end = max(intervals[index - 1].end, intervals[index].end)
                intervals.remove(intervals[index - 1])
                intervals.remove(intervals[index - 1])
                intervals.insert(index - 1, tmp)
            else:
                index += 1

        return intervals

nums = [[1,3],[2,6],[8,10],[15,18]]
#nums = [[1,4],[0,2],[3,5]]
intervals = []
for num in nums:
    tmp = Interval()
    tmp.start = num[0]
    tmp.end = num[1]
    intervals.append(tmp)

s = Solution()
print s.merge(intervals)
