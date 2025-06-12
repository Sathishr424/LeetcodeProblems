# Last updated: 12/6/2025, 5:51:04 am
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val = 0
        for num in nums:
            val ^= num
        
        rightmost_bit = val & -val

        a = b = 0
        for num in nums:
            if num & rightmost_bit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
        
        