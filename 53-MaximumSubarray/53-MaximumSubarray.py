# Last updated: 12/6/2025, 2:34:48 am
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = 0
        prefix = [0]
        for num in nums:
            p += num
            prefix.append(min(p, prefix[-1]))
        
        ret = -float('inf')
        s = 0
        for i, num in enumerate(nums):
            s += num
            ret = max(ret, s - prefix[i])
        
        return ret
            