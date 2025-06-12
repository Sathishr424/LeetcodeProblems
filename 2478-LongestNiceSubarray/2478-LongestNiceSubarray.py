# Last updated: 12/6/2025, 5:37:52 am
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        num = nums[0]
        ret = 1
        curr = 1
        start = 0
        for i in range(1, len(nums)):
            if num & nums[i] == 0:
                curr += 1
                num |= nums[i]
                ret = max(curr, ret)
            else:
                while start < i and num & nums[i] != 0:
                    num ^= nums[start]
                    start += 1
                num |= nums[i]
                curr = (i-start)+1
        
        return ret