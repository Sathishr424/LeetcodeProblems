# Last updated: 8/9/2026, 11:20:57 PM
1class Solution:
2    def canReach(self, start: list[int], target: list[int]) -> bool:
3        x1, y1 = start
4        x2, y2 = target
5        return (abs(x1 - x2) + abs(y1 - y2)) % 2 == 0