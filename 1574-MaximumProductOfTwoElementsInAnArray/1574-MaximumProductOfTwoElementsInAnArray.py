# Last updated: 12/6/2025, 5:41:27 am
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = 0
        second_max = 0

        for num in nums:
            if num >= first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        return (first_max-1) * (second_max-1)
