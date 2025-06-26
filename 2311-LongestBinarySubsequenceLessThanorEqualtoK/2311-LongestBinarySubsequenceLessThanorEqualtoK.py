# Last updated: 26/6/2025, 9:18:33 pm
inf = -float('inf')
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # dp = [[0] * n for _ in range(n)]

        # @cache
        def rec(i, j):
            if i < 0 or j == n: return i + 1

            if s[i] == s[j]:
                return rec(i-1, j + 1)
            
            return i + 1

        ans = [0, 1]
        for i in range(1, n):
            left = rec(i-1, i+1)
            window = (i - left) * 2 + 1
            if window > ans[1]:
                ans = [left, window]
                # print(s[ans[0]:ans[0] + ans[1]])
            left = rec(i-1, i)
            window = (i - left) * 2
            if window > ans[1]:
                ans = [left, window]
                # print(s[ans[0]:ans[0] + ans[1]])
        
        return s[ans[0]:ans[0] + ans[1]]