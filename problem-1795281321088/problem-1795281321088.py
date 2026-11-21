# Last updated: 11/21/2026, 10:45:21 PM
1class Solution:
2    def minRange(self, a: int, b: int, c: int) -> int:
3        def getAns(arr):
4            return max(arr) - min(arr)
5        A = [b + c, b, c]
6        B = [a, a + c, c]
7        C = [a, b, a + b]
8
9        return min([getAns(arr) for arr in [A, B, C, [a, b, c]]])