# Last updated: 12/6/2025, 5:51:01 am
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        for i in range(n+1):
            a ^= i
        
        for num in nums:
            a ^= num
        
        return a