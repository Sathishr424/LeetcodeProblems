# Last updated: 12/25/2025, 7:08:17 PM
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        n = len(s)

        a = s.count('a')
        b = s.count('b')

        return n - (min(a, b) * 2)
            