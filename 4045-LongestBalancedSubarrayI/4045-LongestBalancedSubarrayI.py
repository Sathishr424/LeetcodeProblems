# Last updated: 12/25/2025, 7:08:52 PM
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            if n - i <= best: break
            even = {}
            odd = {}
            for j in range(i, n):
                if nums[j] % 2:
                    odd[nums[j]] = 1
                else:
                    even[nums[j]] = 1
                if len(odd) == len(even):
                    best = max(best, j - i + 1)
        return best