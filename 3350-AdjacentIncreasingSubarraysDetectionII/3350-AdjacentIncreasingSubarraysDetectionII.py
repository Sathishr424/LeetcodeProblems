# Last updated: 15/10/2025, 8:54:37 am
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        increasing = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing[i] = increasing[i - 1] + 1
        
        def isGood(k):
            for i in range(n - (k * 2) + 1):
                if increasing[i + k - 1] >= k-1 and increasing[i + (k * 2) - 1] >= k-1:
                    return True

            return False
        
        l = 0
        r = n // 2

        while l < r:
            mid = (l + r + 1) // 2

            if isGood(mid):
                l = mid
            else:
                r = mid - 1
        
        return l
        