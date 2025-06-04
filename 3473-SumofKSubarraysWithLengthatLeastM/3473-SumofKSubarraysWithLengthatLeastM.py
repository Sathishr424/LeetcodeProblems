# Last updated: 4/6/2025, 10:08:27 pm
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        prefix = []
        p = 0
        n = len(nums)

        for num in nums:
            p += num
            prefix.append(p)
        
        inf = -float('inf')

        @cache
        def rec(index, rem, extend):
            if rem == 0 and index == n: return 0
            if index >= n: return inf

            ans = rec(index+1, rem, False)
            
            prev = prefix[index] - nums[index]

            if extend:
                ans = max(ans, rec(index+1, rem, (index+1)+(rem*m) < n) + nums[index])
            
            if index+m <= n:
                ans = max(ans, rec(index+m, rem-1, (index+m)+((rem-1)*m) < n) + (prefix[index+m-1] - prev))
            return ans
        
        ans = rec(0, k, False)
        rec.cache_clear()
        return ans

        
