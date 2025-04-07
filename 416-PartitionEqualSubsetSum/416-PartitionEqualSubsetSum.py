# Last updated: 7/4/2025, 3:46:24 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2
        # print(half)
        n = len(nums)
        dp = [False] * (half+1)
        dp[0] = True
        # nums.sort()
        for num in nums:
            tmp = dp + []
            for tot in range(0, half):
                if tmp[tot] and tot+num <= half:
                    dp[tot+num] = True
        # print(dp)
        return dp[half]

        
            
            