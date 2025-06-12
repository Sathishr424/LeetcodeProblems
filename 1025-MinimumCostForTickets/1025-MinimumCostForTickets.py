# Last updated: 12/6/2025, 5:44:43 am
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        first = days[0]
        last = days[-1]
        hash = {}
        for day in days: hash[day] = 1
        dp = [float('inf') for _ in range(last+1)]
        dp[first-1] = 0
        for i in range(first, last+1):
            if i in hash:
                dp[i] = min(dp[i], dp[i-1] + costs[0], dp[i-1] + costs[1], dp[i-1] + costs[2])
                if i+6 <= last:
                    dp[i+6] = min(dp[i+6], dp[i-1] + costs[1])
                else:
                    dp[last] = min(dp[last], dp[i-1] + costs[1])
                if i+29 <= last:
                    dp[i+29] = min(dp[i+29], dp[i-1] + costs[2])
                else:
                    dp[last] = min(dp[last], dp[i-1] + costs[2])
            else:
                dp[i] = min(dp[i], dp[i-1])
        return dp[last]
            