# Last updated: 12/6/2025, 5:38:40 am
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        k = 0
        for i in range(n):
            if nums[i] == 1: k += 1
        
        ones = 0
        for i in range(k):
            if nums[i] == 1: ones += 1
        res = k-ones

        for i in range(k, n+k):
            i = i % n
            ones -= nums[i-k] == 1
            ones += nums[i] == 1

            res = min(res, k-ones)

        return res
