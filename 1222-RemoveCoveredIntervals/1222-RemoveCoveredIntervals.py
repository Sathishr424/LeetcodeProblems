# Last updated: 12/6/2025, 5:43:31 am
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        prev = -1
        ret = len(intervals)
        
        for x, y in intervals:
            if y <= prev:
                ret -= 1
            else:
                prev = y
        
        return ret

        