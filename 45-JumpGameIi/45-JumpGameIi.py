# Last updated: 12/6/2025, 5:54:34 am
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        left = nums[0]
        steps = 1

        right = nums[0]

        for i in range(1, n-1):
            left = max(left, nums[i] + i)
            if i >= right:
                right = left
                steps += 1
            if right >= n-1: return steps
        
        return steps