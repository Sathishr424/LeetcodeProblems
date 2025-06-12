# Last updated: 12/6/2025, 5:54:17 am
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: return [newInterval]
        if intervals[0][0] >= newInterval[1]:
            newInterval, intervals[0] = intervals[0], newInterval
        ret = []
        i = 0
        prev = newInterval
        while i < n:
            if intervals[i][1] >= newInterval[0]:
                if intervals[i][0] > newInterval[0]:
                    prev = newInterval
                else:
                    prev = intervals[i]
                    intervals[i] = newInterval
                break
            else:
                ret.append(intervals[i])
            i += 1
        for j in range(i, n):
            if intervals[j][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[j][1])]
            else:
                ret.append(prev)
                prev = intervals[j]
        ret.append(prev)
        return ret