# Last updated: 12/6/2025, 5:51:42 am
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        ret = n+1
        sum = 0

        for i in range(n):
            sum += nums[i]

            while sum >= target:
                ret = min(ret, i - l + 1)
                sum -= nums[l]
                l += 1
        
        return ret if ret <= n else 0