# Last updated: 24/9/2025, 12:15:22 am
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        line = [0] * (max([y for _, y in intervals]) + 2)
        for l, r in intervals:
            line[l] += 1
            line[r + 1] -= 1
        
        best = 0
        curr = 0
        for i in range(len(line)):
            curr += line[i]
            best = max(best, curr)
        
        return best