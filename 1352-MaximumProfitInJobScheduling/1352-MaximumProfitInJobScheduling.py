# Last updated: 12/6/2025, 5:42:46 am
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))

        memo = {}
        def dp(i):
            nonlocal memo
            if i == n: return 0
            if i in memo: return memo[i]
            ans = dp(i + 1)  # Choice 1: Don't pick

            for j in range(i + 1, n + 1):
                if j == n or jobs[j][0] >= jobs[i][1]:
                    ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
                    break
            memo[i] = ans
            return ans

        return dp(0)