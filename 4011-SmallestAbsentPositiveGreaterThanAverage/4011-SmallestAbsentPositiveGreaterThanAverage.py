# Last updated: 12/25/2025, 7:09:11 PM
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        s = sum(nums)
        a = s // n
        
        if a <= 0:
            a = 1
        else:
            a += 1
        
        while a in nums:
            a += 1

        return a
        