# Last updated: 6/10/2025, 6:58:29 pm
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        m = len(nums)

        @cache
        def rec(index, is_small, strict, mask, done):
            if is_small and index == m-1:
                if done:  return 1
                return 0
            
            if index == m:
                if done: return 1
                return 0
            
            ans = 1 if done else 0
            if strict:
                for i in range(10):
                    new_done = done or mask & (1 << i) > 0
                    if i <= nums[index]:
                        ans += rec(index + 1, is_small, i == nums[index], mask | (1 << i), new_done)
                    elif index < m-1:
                        ans += rec(index + 1, 1, 0, mask | (1 << i), new_done)
            else:
                for i in range(10):
                    new_done = done or mask & (1 << i) > 0
                    ans += rec(index + 1, is_small, 0, mask | (1 << i), new_done)
            
            return ans
        
        ans = 0
        for i in range(1, 10):
            ans += rec(1, i > nums[0], i == nums[0], 1 << i, 0)

        rec.cache_clear()
        return ans