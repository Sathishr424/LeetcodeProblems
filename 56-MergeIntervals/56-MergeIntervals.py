# Last updated: 12/6/2025, 5:54:20 am
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        ret = []
        prev = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(intervals[i][1], prev[1])]
            else:
                ret.append(prev)
                prev = intervals[i]
        ret.append(prev)
        return ret