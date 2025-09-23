# Last updated: 24/9/2025, 12:16:14 am
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        line = defaultdict(int)
        for l, r in intervals:
            line[l] += 1
            line[r + 1] -= 1
        
        best = 0
        curr = 0
        for p in sorted(line.keys()):
            curr += line[p]
            best = max(best, curr)
        
        return best