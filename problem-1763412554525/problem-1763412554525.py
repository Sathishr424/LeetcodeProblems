# Last updated: 18/11/2025, 2:19:14 am
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        mod = 10**9 + 7

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(n):
            cnt, mark = types[i]
            for rem in range(target, -1, -1):
                curr = dp[rem]
                for _ in range(cnt):
                    if mark + rem > target: break
                    rem += mark
                    dp[rem] += curr
                    dp[rem] %= mod

        return dp[target]