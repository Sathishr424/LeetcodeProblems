# Last updated: 12/6/2025, 5:36:57 am
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)

        start = 0
        new_start = 0
        ret = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                start = new_start
                new_start = i
            ret = max(ret, i-start+1)

        return ret