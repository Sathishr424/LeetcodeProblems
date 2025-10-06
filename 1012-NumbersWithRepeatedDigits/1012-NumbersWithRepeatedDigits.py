# Last updated: 6/10/2025, 7:10:59 pm
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        m = len(nums)

        @cache
        def rec(pos, strict, leading, mask, done):
            if pos == m:
                if done and not leading:
                    return 1
                return 0
            
            ans = 0
            limit = nums[pos] if strict else 9
            for i in range(0, limit + 1):
                new_done = done or (not leading and mask & (1 << i) > 0)
                new_mask = mask if leading and i == 0 else mask | (1 << i)

                ans += rec(pos + 1, strict and i == nums[pos], leading and i == 0, new_mask, new_done)
            return ans
        
        ans = rec(0, 1, 1, 0, 0)
        rec.cache_clear()
        return ans