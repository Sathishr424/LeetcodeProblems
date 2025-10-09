# Last updated: 9/10/2025, 8:40:14 am
cmin = lambda x, y: x if x < y else y
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        # 0,  5,  30, 40, 60
        # 60, 61, 66, 68, 72

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + skill[i - 1] * mana[0]

        for j in range(1, m):
            a = dp[-1]
            min_diff = a - dp[1]
            for i in range(1, n):
                a += skill[i - 1] * mana[j]
                min_diff = cmin(min_diff, a - dp[i + 1])
            dp[0] = dp[-1] - min_diff
            for i in range(1, n + 1):
                dp[i] = dp[i - 1] + skill[i - 1] * mana[j]

        return dp[-1]