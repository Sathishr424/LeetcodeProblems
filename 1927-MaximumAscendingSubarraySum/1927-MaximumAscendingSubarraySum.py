# Last updated: 12/6/2025, 5:39:47 am
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = curr
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
                ans = max(curr, ans)
            else:
                curr = nums[i]

        return ans