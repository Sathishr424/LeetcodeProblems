# Last updated: 3/5/2025, 5:20:39 pm
cmin = lambda x, y: x if x < y else y
inf = 15
class Solution:
    def minSessions(self, tasks: List[int], sTime: int) -> int:
        n = len(tasks)
        full_mask = (1 << (n+1)) - 1
        start_mask = 1 << n

        diff = full_mask - start_mask

        dp = [[inf] * (sTime+1) for _ in range(diff+1)]

        dp[0][0] = 0
    
        for mask in range(start_mask, full_mask):
            for time in range(sTime+1):
                for i in range(n):
                    if mask & (1 << i) == 0:
                        new_mask = mask | (1 << i)
                        if time >= tasks[i]:
                            dp[new_mask-start_mask][time-tasks[i]] = cmin(dp[new_mask-start_mask][time-tasks[i]], dp[mask-start_mask][time])
                        else:
                            dp[new_mask-start_mask][sTime-tasks[i]] = cmin(dp[new_mask-start_mask][sTime-tasks[i]], dp[mask-start_mask][time] + 1)
        
        return min(dp[full_mask-start_mask])

