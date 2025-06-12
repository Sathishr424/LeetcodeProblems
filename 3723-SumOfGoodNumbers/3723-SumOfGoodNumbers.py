# Last updated: 12/6/2025, 5:34:55 am
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        
        for i in range(n):
            if (i-k < 0 or nums[i] > nums[i-k]) and (i+k >= n or nums[i] > nums[i+k]):
                ret += nums[i]

        return ret
            