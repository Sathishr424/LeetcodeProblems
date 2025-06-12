# Last updated: 12/6/2025, 5:41:23 am
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        ones = 0
        ret = 0

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                if zero != -1:
                    ret = max(ret, ones)
                    ones = i-zero-1
                zero = i
            else:
                ones += 1
        
        if zero == -1: return max(ret, ones-1)
        return max(ret, ones)