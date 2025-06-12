# Last updated: 12/6/2025, 5:48:11 am
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = m
        y = n

        for i,j in ops:
            x = min(i, x)
            y = min(j, y)
        
        return x*y