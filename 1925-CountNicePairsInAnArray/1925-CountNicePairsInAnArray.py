# Last updated: 12/6/2025, 5:39:50 am
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        @lru_cache
        def reverse(num):
            r = 0
            while num > 0:
                r = (r * 10) + (num % 10)
                num = num // 10
            return r
        
        mod = (10**9) + 7
        hash = defaultdict(int)
        ret = 0
    
        for num in nums:
            rev = num - reverse(num)
            ret = (ret + hash[rev]) % mod
            hash[rev] += 1

        return ret