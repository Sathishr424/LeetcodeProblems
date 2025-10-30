# Last updated: 30/10/2025, 8:45:56 pm
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n == 3: return 0

        ans = nums[-2] - nums[1]
        ans = min(ans, nums[-1] - nums[2])
        ans = min(ans, nums[-3] - nums[0])

        return ans
            
        