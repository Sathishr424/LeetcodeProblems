# Last updated: 4/8/2025, 2:29:08 pm
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor