# Last updated: 18/5/2025, 5:18:21 pm
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            s = 0
            while num:
                s += num % 10
                num //= 10
            if s == i: return i
        
        return -1