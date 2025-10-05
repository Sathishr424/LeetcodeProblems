# Last updated: 6/10/2025, 12:20:17 am
class Solution:
    def countDigitOne(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        m = len(nums)

        @cache
        def rec(index, strict, add, cnt):
            if index == m:
                return cnt
            
            ans = cnt if add else 0
            if strict:
                for i in range(10):
                    if i > nums[index]: break
                    ans += rec(index + 1, i == nums[index], add, cnt + (i == 1))
            else:
                for i in range(10):
                    ans += rec(index + 1, 0, add, cnt + (i == 1))
            
            return ans
        
        ans = 0
        for i in range(1, nums[0] + 1):
            ans += rec(1, i == nums[0], 0, 1 if i == 1 else 0)
        
        if 2 <= m:
            for i in range(1, 10):
                ans += rec(2, 0, 1, 1 if i == 1 else 0)

        rec.cache_clear()
        return ans