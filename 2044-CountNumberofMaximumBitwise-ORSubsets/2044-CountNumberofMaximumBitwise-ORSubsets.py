# Last updated: 28/7/2025, 12:11:51 pm
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        for num in nums:
            maxi |= num
        
        @cache
        def rec(index, s):
            if index == n:
                if s == maxi: return 1
                return 0
            
            ans = rec(index + 1, s)
            ans += rec(index + 1, s | nums[index])
            return ans
        
        return rec(0, 0)