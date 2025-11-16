# Last updated: 16/11/2025, 8:07:39 am
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        n = len(s)

        a = s.count('a')
        b = s.count('b')

        return n - (min(a, b) * 2)
            