# Last updated: 12/6/2025, 5:48:00 am
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        tot = 0
        ret = -float('inf')

        for i in range(k):
            tot += nums[i]

        for i in range(k, n):
            ret = max(ret, tot)
            tot += nums[i]
            tot -= nums[i-k]
        
        return max(ret, tot) / k