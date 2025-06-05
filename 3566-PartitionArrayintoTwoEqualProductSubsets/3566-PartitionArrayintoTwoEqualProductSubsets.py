# Last updated: 5/6/2025, 4:58:42 pm
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        memo = {}
        
        def rec(mask, tot, rem):
            if mask in memo: return memo[mask]
            if tot == target:
                return rem == target

            for i in range(n):
                if mask & (1 << i) == 0 and rec(mask | (1 << i), tot * nums[i], rem // nums[i]): 
                    memo[mask] = True
                    return True
            
            memo[mask] = False
            return False
        
        total = 1
        for num in nums:
            total *= num
        
        return rec(0, 1, total)