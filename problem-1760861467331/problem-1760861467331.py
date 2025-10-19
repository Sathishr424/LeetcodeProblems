# Last updated: 19/10/2025, 1:41:07 pm
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