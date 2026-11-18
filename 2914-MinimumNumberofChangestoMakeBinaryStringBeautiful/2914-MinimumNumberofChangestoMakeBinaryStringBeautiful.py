# Last updated: 11/18/2026, 3:42:36 PM
1class Solution:
2    def minChanges(self, s: str) -> int:
3        return sum([1 for i in range(0, len(s), 2) if s[i] != s[i+1]])