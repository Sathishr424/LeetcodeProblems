# Last updated: 12/6/2025, 5:45:19 am
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        minSum = nums[0]
        maxSum = nums[0]
        resMin = minSum
        resMax = maxSum

        for i in range(1, len(nums)):
            minSum += nums[i]
            maxSum += nums[i]

            if nums[i] < minSum:
                minSum = nums[i]
            if nums[i] > maxSum:
                maxSum = nums[i]
            resMin = min(resMin, minSum)
            resMax = max(resMax, maxSum)
            total += nums[i]
        if resMin == total: return resMax
        return max(total-resMin, resMax)