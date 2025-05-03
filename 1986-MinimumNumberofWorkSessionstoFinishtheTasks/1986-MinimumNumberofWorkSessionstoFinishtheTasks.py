# Last updated: 3/5/2025, 5:13:57 pm
class Solution:
    def minSessions(self, tasks: List[int], sTime: int) -> int:
        n = len(tasks)
        full_mask = (1 << (n+1)) - 1
        start_mask = 1 << n

        dp = [[float('inf')] * (sTime+1) for _ in range(full_mask+1)]

        dp[start_mask][0] = 0
    
        for mask in range(start_mask, full_mask):
            for time in range(sTime+1):
                for i in range(n):
                    if mask & (1 << i) == 0:
                        new_mask = mask | (1 << i)
                        if time >= tasks[i]:
                            dp[new_mask][time-tasks[i]] = min(dp[new_mask][time-tasks[i]], dp[mask][time])
                        else:
                            dp[new_mask][sTime-tasks[i]] = min(dp[new_mask][sTime-tasks[i]], dp[mask][time] + 1)
        
        # print(dp[full_mask])
        return min(dp[full_mask])

