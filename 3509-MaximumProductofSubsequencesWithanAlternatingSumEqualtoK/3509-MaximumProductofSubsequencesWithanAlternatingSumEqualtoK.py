# Last updated: 15/7/2025, 2:42:15 pm
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        zero_index = -1
        for i, num in enumerate(nums):
            if num == 0:
                zero_index = i
        @cache
        def rec(index, is_odd, s, lim, zero_used):
            # print(index, is_odd, s, lim)
            if index == n: 
                if s == k: 
                    if lim == 0: 
                        if zero_used: return 0
                        return -inf
                    return lim
                return -inf
            
            ans = rec(index + 1, is_odd, s, lim, zero_used)
            if lim * nums[index] <= limit:
                if is_odd:
                    s -= nums[index]
                else:
                    s += nums[index]
                ans = max(ans, rec(index + 1, not is_odd, s, lim * nums[index], zero_used or nums[index] == 0))
            elif index <= zero_index:
                if is_odd:
                    s -= nums[index]
                else:
                    s += nums[index]
                ans = max(ans, rec(index + 1, not is_odd, s, 0, zero_used or nums[index] == 0))
            
            return ans
        
        ans = -inf
        for i in range(n):
            if nums[i] <= limit:
                ans = max(ans, rec(i + 1, True, nums[i], nums[i], nums[i] == 0))
        if ans == -inf: return -1
        rec.cache_clear()
        return ans