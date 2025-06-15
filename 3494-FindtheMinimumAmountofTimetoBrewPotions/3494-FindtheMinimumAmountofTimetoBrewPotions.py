# Last updated: 15/6/2025, 10:01:44 am
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        
        start = 0
        dp = [start]
        for j in range(n):
            start += skill[j] * mana[0]
            dp.append(start)

        for i in range(1, m):
            min_diff = start - dp[1]
            prev = start
            for j in range(n):
                min_diff = min(min_diff, start - dp[j+1])
                start += skill[j] * mana[i]

            start = prev - min_diff
            dp[0] = start
            for j in range(n):
                start += skill[j] * mana[i]
                dp[j+1] = start
        
        return dp[-1]