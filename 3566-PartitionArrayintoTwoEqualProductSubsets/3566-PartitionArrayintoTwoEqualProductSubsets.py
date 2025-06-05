# Last updated: 5/6/2025, 4:57:00 pm
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        @cache
        def rec(mask, tot, rem):
            if tot == target:
                return rem == target

            for i in range(n):
                if mask & (1 << i) == 0 and rec(mask | (1 << i), tot * nums[i], rem // nums[i]): return True

            return False
        
        total = 1
        for num in nums:
            total *= num
        
        return rec(1 << n, 1, total)