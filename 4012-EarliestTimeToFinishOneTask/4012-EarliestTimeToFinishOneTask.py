# Last updated: 12/25/2025, 7:09:10 PM
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        e_time = inf
        for s, e in tasks:
            e_time = min(e_time, s + e)

        return e_time