# Last updated: 7/4/2025, 3:58:13 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2

        # Bottom up
        dp = [False] * (half+1)
        dp[0] = True

        for num in nums:
            for tot in range(half-num, -1, -1):
                if dp[tot]:
                    dp[tot+num] = True

        return dp[half]

        # Top down
        n = len(nums)

        nums.sort()
        @cache
        def rec(index, tot):
            if tot == half: return True
            if tot > half or index == n: return False

            return rec(index+1, tot+nums[index]) or rec(index+1, tot)
        
        return rec(0, 0)

        
            
            