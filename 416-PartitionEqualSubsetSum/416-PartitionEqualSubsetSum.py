# Last updated: 7/4/2025, 3:03:55 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2

        n = len(nums)

        nums.sort()
        @cache
        def rec(index, tot):
            if tot == half: return True
            if tot > half or index == n: return False

            return rec(index+1, tot+nums[index]) or rec(index+1, tot)
        
        return rec(0, 0)
            
            