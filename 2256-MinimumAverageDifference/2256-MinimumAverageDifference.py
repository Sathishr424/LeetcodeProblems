# Last updated: 11/9/2025, 10:49:41 pm
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_diff = inf
        index = -1

        right = sum(nums)
        left = 0
        for i in range(n):
            left += nums[i]
            right -= nums[i]

            if right == 0:
                diff = left // (i + 1)
            else:
                diff = abs((right // (n - i - 1)) - (left // (i + 1)))
            
            if diff < min_diff:
                index = i
                min_diff = diff
        
        return index
