# Last updated: 14/10/2025, 1:43:39 pm
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        increasing = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing[i] = increasing[i - 1] + 1
        
        for i in range(n - (k * 2) + 1):
            if increasing[i + k - 1] >= k-1 and increasing[i + (k * 2) - 1] >= k-1:
                return True

        return False