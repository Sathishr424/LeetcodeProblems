# Last updated: 16/11/2025, 8:01:48 am
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