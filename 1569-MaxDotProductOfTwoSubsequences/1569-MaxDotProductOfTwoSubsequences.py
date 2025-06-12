# Last updated: 12/6/2025, 5:41:31 am
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        m = len(nums1)
        dp = [-float('inf')] * (n+1)
        
        for i in range(m-1, -1, -1):
            prev = dp[n]
            for j in range(n-1, -1, -1):
                x = nums1[i] * nums2[j]
                tmp = dp[j]
                dp[j] = max(prev+x, x, dp[j], dp[j+1])
                prev = tmp

        return dp[0]