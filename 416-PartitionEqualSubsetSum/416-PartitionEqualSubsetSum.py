# Last updated: 9/5/2025, 8:20:39 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        half = total // 2
        n = len(nums)
        nums.sort()

        @cache
        def rec(index, tot):
            if index == n: return False
            if tot >= half: return tot == half

            return rec(index+1, tot+nums[index]) or rec(index+1, tot)
        
        return rec(0, 0)