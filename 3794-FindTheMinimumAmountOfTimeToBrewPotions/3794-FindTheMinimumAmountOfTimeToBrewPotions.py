# Last updated: 12/6/2025, 5:34:10 am
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        dp = [0] * (n+1)
        diff = 0

        for j in range(m):
            dp[0] = dp[-1]
            diff = float('inf')
            for i in range(1, n+1):
                diff = min(diff, dp[i-1] - dp[i])
                dp[i] = dp[i-1] + (mana[j] * skill[i-1])
            for i in range(1, n+1):
                dp[i] -= diff
            # print(dp, diff)
            # diff = new_diff
        
        return dp[-1]