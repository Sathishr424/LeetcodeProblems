# Last updated: 12/6/2025, 5:42:37 am
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = (10**9) + 7
        memo = {}
        ret = 0
        def rec(pos, step):
            if pos == 0 and step == 0: return 1
            elif pos < 0 or step < 0 or pos > step or pos >= arrLen: return 0
            elif (pos, step) in memo: return memo[(pos, step)]

            memo[(pos, step)] = rec(pos+1, step-1) + rec(pos-1, step-1) + rec(pos, step-1)
            return memo[(pos, step)]
        return rec(0, steps) % mod
