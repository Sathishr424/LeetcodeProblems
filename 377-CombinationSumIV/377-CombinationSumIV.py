# Last updated: 9/5/2025, 7:39:18 pm
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @cache
        def rec(tot):
            if tot == target: return 1
            ans = 0
            for num in nums:
                if num+tot > target: break
                ans += rec(tot+num)
            
            return ans
        
        return rec(0)