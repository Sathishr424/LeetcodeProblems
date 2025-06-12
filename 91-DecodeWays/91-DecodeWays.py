# Last updated: 12/6/2025, 5:53:30 am
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ret = 0
        memo = {}
        def rec(index):
            if index == n: return 1
            if s[index] == '0': return 0
            if index in memo: return memo[index]
            memo[index] = 0
            memo[index] += rec(index+1)
            if index+1 < n and int(s[index:index+2]) <= 26:
                memo[index] += rec(index+2)
            return memo[index]
        return rec(0)