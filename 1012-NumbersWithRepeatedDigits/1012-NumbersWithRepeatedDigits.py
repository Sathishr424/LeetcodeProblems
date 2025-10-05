# Last updated: 6/10/2025, 12:03:49 am
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        m = len(nums)

        @cache
        def rec(index, strict, add, mask, done):
            if index == m:
                if done: return 1
                return 0
            
            ans = add if done else 0
            if strict:
                for i in range(10):
                    if i > nums[index]: break
                    new_done = done or mask & (1 << i) > 0
                    ans += rec(index + 1, i == nums[index], add, mask | (1 << i), new_done)
            else:
                for i in range(10):
                    new_done = done or mask & (1 << i) > 0
                    ans += rec(index + 1, 0, add, mask | (1 << i), new_done)
            
            return ans
        
        ans = 0
        for i in range(1, nums[0] + 1):
            ans += rec(1, i == nums[0], 0, 1 << i, 0)
        
        if 2 <= m:
            for i in range(1, 10):
                ans += rec(2, 0, 1, 1 << i, 0)

        rec.cache_clear()
        return ans