# Last updated: 16/9/2025, 5:16:22 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
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

        def isGood(mid):
            # dp = [[inf] * (1 << n) for _ in range(k + 1)]

            @cache
            def rec(mask, rem):
                if rem == 0:
                    return mask == full_mask
                
                for new_mask in c_masks[mask]:
                    if masks[new_mask] <= mid and rec(mask | new_mask, rem - 1):
                        return True
                
                return False
            rec.cache_clear()
        
            return rec(0, k)

        l = max(jobs)
        r = sum(jobs[:n-(k-1)])

        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
