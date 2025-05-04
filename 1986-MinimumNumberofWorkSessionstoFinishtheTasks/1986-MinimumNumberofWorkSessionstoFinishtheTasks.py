# Last updated: 4/5/2025, 10:49:11 am
inf = 15
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        full_mask = (1 << (n+1)) - 1
        dp = [[inf] * sessionTime for _ in range(full_mask)]

        def rec(mask, remTime):
            if mask == full_mask: return 0
            if dp[mask][remTime] != inf: return dp[mask][remTime] 
            ans = inf
            for i in range(n):
                if mask & (1 << i) == 0:
                    if tasks[i] <= remTime:
                        ans = min(ans, rec(mask | (1 << i), remTime - tasks[i]))
                    else:
                        ans = min(ans, rec(mask | (1 << i), sessionTime - tasks[i]) + 1)
            dp[mask][remTime]  = ans
            return ans
        
        return rec(1 << n, 0)

