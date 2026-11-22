# Last updated: 11/22/2026, 10:08:54 AM
1class Solution:
2    def checkString(self, s: str) -> bool:
3        a = s.count('a')
4        for c in s:
5            if c == 'a': a -= 1
6            elif a > 0: return False
7
8        return True