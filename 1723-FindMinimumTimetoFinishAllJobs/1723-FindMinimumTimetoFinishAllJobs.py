# Last updated: 16/9/2025, 5:03:04 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        full_mask = (1 << n) - 1

        masks = [0] * (1 << n)
        for mask in range(1, 1 << n):
            c = 0
            for i in range(n):
                if mask & (1 << i):
                    c += jobs[i]
            masks[mask] = c
        
        c_masks = [[] for _ in range(1 << n)]
        for mask in range(1 << n):
            for new_mask in range(mask + 1, 1 << n):
                if mask & new_mask == 0:
                    c_masks[mask].append(new_mask)

        dp = [[inf] * (1 << n) for _ in range(k + 1)]
        dp[0][0] = 0

        for rem in range(1, k + 1):
            for mask in range(1 << n):
                val = dp[rem - 1][mask]
                if val == inf: continue
                for new_mask in c_masks[mask]:
                    mask_ = mask | new_mask
                    dp[rem][mask_] = cmin(dp[rem][mask_], cmax(val, masks[new_mask]))

        # [print(row) for row in dp]
        return dp[-1][full_mask]