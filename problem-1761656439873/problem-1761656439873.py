# Last updated: 28/10/2025, 6:30:39 pm
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def isGood(mid):
            dp = [0] * (n + 2)
            maxi = 0
            for i in range(2, n + 2):
                if nums[i - 2] <= mid:
                    dp[i] = max(dp[i - 2] + 1, dp[i - 1])
                    maxi = max(maxi, dp[i])
                else:
                    dp[i] = max(dp[i-2], dp[i-1])

            return maxi >= k
            
        l = min(nums)
        r = max(nums)

        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        return l