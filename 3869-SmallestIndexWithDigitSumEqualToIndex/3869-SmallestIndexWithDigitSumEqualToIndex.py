# Last updated: 12/6/2025, 5:33:18 am
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            s = 0
            while num:
                s += num % 10
                num //= 10
            if s == i: return i
        
        return -1