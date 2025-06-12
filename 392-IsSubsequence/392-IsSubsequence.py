# Last updated: 12/6/2025, 5:49:56 am
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        index = 0
        for i in range(n):
            if index < m and t[i] == s[index]:
                index += 1
        
        return index == m