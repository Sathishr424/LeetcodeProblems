# Last updated: 12/25/2025, 7:08:09 PM
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k: continue
                    ans = max(ans, nums[i] + nums[j] - nums[k])

        return ans