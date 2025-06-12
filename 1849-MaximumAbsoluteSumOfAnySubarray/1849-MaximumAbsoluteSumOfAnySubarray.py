# Last updated: 12/6/2025, 5:40:06 am
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = abs(nums[0])
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum+nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        
        currSum = -nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum-nums[i], -nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum
        