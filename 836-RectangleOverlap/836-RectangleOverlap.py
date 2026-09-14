# Last updated: 9/14/2026, 5:31:09 PM
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        if (rec1[0]>=rec2[2] or rec2[0]>=rec1[2]): return False
4        if (rec1[1]>=rec2[3] or rec2[1]>=rec1[3]): return False
5        return True