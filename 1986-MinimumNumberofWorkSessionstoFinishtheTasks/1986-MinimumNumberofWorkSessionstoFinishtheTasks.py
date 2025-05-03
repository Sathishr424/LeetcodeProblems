# Last updated: 3/5/2025, 4:54:38 pm
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        full_mask = (1 << (n+1)) - 1
        @cache
        def rec(mask, remTime):
            if mask == full_mask: return 0
            ans = float('inf')
            for i in range(n):
                if mask & (1 << i) == 0:
                    if tasks[i] <= remTime:
                        ans = min(ans, rec(mask | (1 << i), remTime - tasks[i]))
                    else:
                        ans = min(ans, rec(mask | (1 << i), sessionTime - tasks[i]) + 1)
            return ans
        
        return rec(1 << n, 0)

